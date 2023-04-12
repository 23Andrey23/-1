import requests
import json


class ApiPets:

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
        со списком наденых питомцев, совпадающих с фильтром"""

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

    def post_api_create_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Этот запрос позволяет добавить инфориацию о новом питомце"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        hedears = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + '/api/create_pet_simple', headers=hedears, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def post_api_pets_set_photo_pet_id(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Этот запрос позволяет добавить фотографию домашнего животного"""

        heders = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}

        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=heders, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def post_api_pets_set_photo_pet_id_not_valid_photo(self, auth_key: json, pet_id: str) -> json:
        """Этот запрос отравляет на добавление фотографии, без фотографии домашнего животного"""

        heders = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=heders)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

