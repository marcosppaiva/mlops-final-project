import pandas as pd
import pytest

from src.training.train import read_data


@pytest.fixture(name='fake_dataframe')
def setup_fake_dataframe():
    data = {
        'company': ['Anúncio Particular', 'Company A'],
    }
    return pd.DataFrame(data)


def test_read_data(fake_dataframe, mocker):
    mocker.patch('pandas.read_parquet', return_value=fake_dataframe)

    result = read_data.fn('dummy_filename.parquet')

    expected_columns = ['company', 'property_ads']
    assert result.columns.tolist() == expected_columns

    assert result['property_ads'].tolist() == [
        'private',
        'private' if property == 'Anúncio Particular' else 'private',
    ]
