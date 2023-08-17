import json
from unittest.mock import patch

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from src.api.main import app, lazy_load_model


class MockDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@pytest.fixture(name='client')
def setup_client():
    return TestClient(app)


@patch('src.api.main.load_model')
@patch('src.api.main.predict')
@patch('src.api.main.save_predictions')
def test_predict_endpoint(mock_save_predictions, mock_predict, mock_load_model, client):
    # Configurar o mock para retornar um modelo falso
    mock_load_model.return_value = ('fake_model', 'fake_preprocessor', 'fake_run_id')

    # Configurar o mock para retornar uma tupla de predição falsa
    fake_price_predict = [1000.0]
    fake_df_data = MockDataFrame(
        {'data': [1, 2, 3]}
    )  # Use o seu DataFrame simulado aqui
    mock_predict.return_value = (fake_price_predict, fake_df_data)

    # Forçar o carregamento do modelo antes de fazer a requisição
    lazy_load_model()

    mock_imovel = {
        'district': 'Lisboa',
        'property_type': 'apartamento',
        'bathroom': 1,
        'metric': 100,
        'room': 2,
        'energy_certify': 'E',
        'condition': 'Ruína',
    }
    response = client.post('/predict', json=mock_imovel)

    assert response.status_code == 200
    assert 'predictions' in response.json()
    assert json.loads(response.json()['predictions'])['price_predicted']['0'] == 1000.0

    mock_save_predictions.assert_called_once_with(fake_df_data)
