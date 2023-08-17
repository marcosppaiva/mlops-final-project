from unittest.mock import Mock

import pytest

from src.scrapper.scrapper import get_infos


@pytest.fixture(name='mock_soup')
def setup_mock_soup(mocker):
    return mocker.Mock()


def test_get_infos(mock_soup, mocker):
    mock_get_attribute_safe = mocker.patch(
        'src.scrapper.scrapper.get_attribute_safe',
        side_effect=[
            '1000 €',
            'Certificado Energético',
            '100 m²',
            'Descrição',
            'Localização: Algum Lugar',
            '2 quartos',
            'Detalhes',
            'Empresa',
        ],
    )

    mock_article = mock_soup.find_all.return_value = [Mock()]

    result = get_infos.fn(mock_soup)

    assert len(result) == 1

    expected_calls = [
        mocker.call(mock_article[0], 'li', {'class': 'offer-item-price'}),
        mocker.call(mock_article[0], 'div', {'class': 'energy-certify'}),
        mocker.call(mock_article[0], 'strong', {'class': 'visible-xs-block'}),
        mocker.call(mock_article[0], 'span', {'class': 'offer-item-title'}),
        mocker.call(mock_article[0], 'p', {'class': 'text-nowrap'}),
        mocker.call(mock_article[0], 'li', {'class': 'offer-item-rooms hidden-xs'}),
        mocker.call(
            mock_article[0], 'ul', {'class': 'params-small clearfix hidden-xs'}
        ),
        mocker.call(mock_article[0], 'img', {'company-logo lazy'}),
    ]
    assert mock_get_attribute_safe.call_args_list == expected_calls
