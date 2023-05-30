import os
import pytest
from utils.function import load_operations, get_last, sorting_operations, card_number_masking


@pytest.fixture
def test_data():
    return load_operations(os.path.join('tests', 'test_operations.json'))


def test_load_data():
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {
                "amount": "70946.18",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366"
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        }
    ]

    assert load_operations(os.path.join('tests', 'test_operations.json')) == expected_result


def test_get_last(test_data):
    expected_result = [{'date': '2018-07-11T02:26:18.671407',
                        'description': 'Открытие вклада',
                        'id': 596171168,
                        'operationAmount': {'amount': '79931.03',
                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 72082042523231456215'},
                       {'date': '2018-08-19T04:27:37.904916',
                        'description': 'Перевод с карты на карту',
                        'from': 'Visa Classic 6831982476737658',
                        'id': 895315941,
                        'operationAmount': {'amount': '56883.54',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Visa Platinum 8990922113665229'},
                       {'date': '2019-07-12T20:41:47.882230',
                        'description': 'Перевод организации',
                        'from': 'Счет 48894435694657014368',
                        'id': 522357576,
                        'operationAmount': {'amount': '51463.70',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 38976430693692818358'},
                       {'date': '2018-12-20T16:43:26.929246',
                        'description': 'Перевод организации',
                        'from': 'Счет 10848359769870775355',
                        'id': 214024827,
                        'operationAmount': {'amount': '70946.18',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 21969751544412966366'},
                       {'date': '2019-03-23T01:09:46.296404',
                        'description': 'Перевод со счета на счет',
                        'from': 'Счет 44812258784861134719',
                        'id': 873106923,
                        'operationAmount': {'amount': '43318.34',
                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 74489636417521191160'}]

    assert get_last(test_data) == expected_result


def test_sorted(test_data):
    expected_result = [{'date': '2019-07-12T20:41:47.882230',
                        'description': 'Перевод организации',
                        'from': 'Счет 48894435694657014368',
                        'id': 522357576,
                        'operationAmount': {'amount': '51463.70',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 38976430693692818358'},
                       {'date': '2019-03-23T01:09:46.296404',
                        'description': 'Перевод со счета на счет',
                        'from': 'Счет 44812258784861134719',
                        'id': 873106923,
                        'operationAmount': {'amount': '43318.34',
                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 74489636417521191160'},
                       {'date': '2018-12-20T16:43:26.929246',
                        'description': 'Перевод организации',
                        'from': 'Счет 10848359769870775355',
                        'id': 214024827,
                        'operationAmount': {'amount': '70946.18',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 21969751544412966366'},
                       {'date': '2018-08-19T04:27:37.904916',
                        'description': 'Перевод с карты на карту',
                        'from': 'Visa Classic 6831982476737658',
                        'id': 895315941,
                        'operationAmount': {'amount': '56883.54',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Visa Platinum 8990922113665229'},
                       {'date': '2018-07-11T02:26:18.671407',
                        'description': 'Открытие вклада',
                        'id': 596171168,
                        'operationAmount': {'amount': '79931.03',
                                            'currency': {'code': 'RUB', 'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 72082042523231456215'}]

    assert sorting_operations(get_last(test_data)) == expected_result


def test_card_number_masking(test_data):
    assert card_number_masking('МИР 5211274343558469') == "МИР 5211 27** ****8469"