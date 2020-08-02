import requests
from functools import wraps
import json

CONNECTION = 'https://recruitment_api.ru'


def api_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('\n')
        check_code = kwargs.pop('check_code') if kwargs.get(
            'check_code') else None  # извлекаем для того чтоб дальше не передать в функцию
        result = func(*args, **kwargs)
        if check_code:
            print('Assert result and expected code: \n result_code: {} = expected code:{} '.format(result.status_code,
                                                                                                   check_code))
            assert (result.status_code == check_code)
        print('Call API:{}'.format(result.url))
        print('Result is: {}'.format(result.json()))
        return result

    return wrapper


@api_check
def create_task(file, changer, change_value):
    with open(file, encoding='utf-8') as raw_test_data:
        test_data = json.load(raw_test_data)
        if changer is not None:  # для тестов с полными данными параметр будет None
            test_data[changer] = change_value  # для тестов с неполными данными принял "0" как условный None или
            # Null,для негативных кейсов будет заменяться на некорректные значения
        response = requests.post(CONNECTION, data=test_data)
        return response
