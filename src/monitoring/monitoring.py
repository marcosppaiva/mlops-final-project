import os
import logging
from typing import Tuple

import pandas as pd
from dotenv import load_dotenv
from prefect import flow, task
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import (
    DataDriftTable,
    ColumnDriftMetric,
    DatasetDriftMetric,
    DatasetMissingValuesMetric,
)

from src.utils.predictions_utils import (
    load_model,
    prepare_data,
    save_metrics,
    load_predictions,
)

load_dotenv()

REF_DATA_PATH = os.getenv('VAL_DATA_PATH', 'data/processed/val.parquet')

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s"
)

model, preprocessor, run_id = load_model()

numerical_columns = ['metric', 'rooms', 'bathroom']
categorical_columns = ['energy_certify', 'property_type', 'district', 'condition']


@task
def load_data(
    ref_filename: str, current_window_size: int = 100
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    current_data = load_predictions(current_window_size)

    ref_data = pd.read_parquet(ref_filename)

    ref_data = ref_data[numerical_columns + categorical_columns]

    return current_data, ref_data


@task
def get_ref_data(filename: str = REF_DATA_PATH):
    df_ref = pd.read_parquet(filename)
    return df_ref


@task
def prep_ref_data(df_ref: pd.DataFrame):
    data_transformed, _ = prepare_data(df_ref, preprocessor)

    pred_prices = model.predict(data_transformed)

    df_ref['price_predicted'] = [round(pred) for pred in pred_prices]

    return df_ref


def get_column_mapping() -> ColumnMapping:

    column_mapping = ColumnMapping()
    column_mapping.target = None
    column_mapping.prediction = 'price_predicted'
    column_mapping.numerical_features = numerical_columns
    column_mapping.categorical_features = categorical_columns

    return column_mapping


@task
def build_report(reference_data, current_data, column_mapping):
    report = Report(
        metrics=[
            ColumnDriftMetric(column_name="price_predicted"),
            DatasetDriftMetric(),
            DatasetMissingValuesMetric(),
            DataDriftTable(),
        ]
    )
    report.run(
        reference_data=reference_data,
        current_data=current_data,
        column_mapping=column_mapping,
    )
    report_path = 'reports/drift_v2.html'
    report.save_html(report_path)

    return report


@task
def calculate_metrics_postgresql(result: dict):
    data = {
        'drift_score': [result['metrics'][0]['result']['drift_score']],
        'drift_detected': [result['metrics'][0]['result']['drift_detected']],
        'number_of_columns': [result['metrics'][1]['result']['number_of_columns']],
        'number_of_drifted_columns': [
            result['metrics'][1]['result']['number_of_drifted_columns']
        ],
        'share_of_missing_values': [
            round(result['metrics'][2]['result']['current']['share_of_missing_values'])
        ],
    }

    return pd.DataFrame(data)


@task
def save_metrics_postgres(metrics: pd.DataFrame):
    save_metrics(metrics)


@flow
def monitoring_flow():
    current_data, ref_data = load_data(REF_DATA_PATH)

    ref_data = prep_ref_data(ref_data)
    num_cols = ['metric', 'rooms', 'bathroom', 'price_predicted']
    cat_cols = ['energy_certify', 'property_type', 'district', 'condition']

    ref_data = current_data[num_cols + cat_cols]
    ref_data = ref_data[num_cols + cat_cols]

    column_mapping = get_column_mapping()
    report = build_report(ref_data, current_data, column_mapping)
    metrics = calculate_metrics_postgresql(report.as_dict())
    save_metrics_postgres(metrics)


if __name__ == '__main__':
    monitoring_flow()
