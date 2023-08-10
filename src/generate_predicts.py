import pandas as pd

from utils.predictions_utils import predict, load_model, save_predictions

model, preprocessor, run_id = load_model()


DATA_PATH = 'data/processed/data.parquet'


if __name__ == '__main__':
    df = pd.read_parquet(DATA_PATH)

    numerical_columns = ['metric', 'rooms', 'bathroom']
    categorical_columns = ['energy_certify', 'property_type', 'district', 'condition']

    df = df[numerical_columns + categorical_columns]

    print('>>>>>>', df.shape)

    preds, _ = predict(df, model, preprocessor)
    print(len(preds))

    df['price_predicted'] = [round(pred) for pred in preds]
    df['model_version'] = run_id

    save_predictions(df)
