import requests
import json
import os


class ApiPet:

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def get_api_key(self, email: str, password: str) -> json:
        """"Метод делает запрос к серверу API и возвращает статус запроса и результат в формате
JSON с уникальным ключом пользователя, найденным по указанной электронной почте и паролем"""

        headers = {
            "email": email,
            "password": password
        }

        res = requests.get(self.base_url + '/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_pets(self, auth_key: json, filter: str) -> json:
        """Метод делает запрос к серверу API и возвращает статус запроса и результат в формате JSON
со списком наденых питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
либо пустое значение - получить список всех питомцев, или 'my_pets' - получить список
свои питомцы"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + '/api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_pets(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запрос на сервер и результат в формате JSON с данными добавленного питомца"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def put_api_pets(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет запрос на сервер об обновлении данных питомуа по указанному идентификатору и
        возвращает статус запроса и результат в формате JSON с обновленными данными о питомце"""

        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type,
        }
        headers = {'auth_key': auth_key['key']}

        res = requests.put(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_api_pets(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному идентификатору и возвращает
        статус запроса и результат в формате JSON с текстом уведомления об успешном удалении."""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
