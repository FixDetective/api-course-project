from dotenv import load_dotenv
import os
import requests

load_dotenv()
YD_API_KEY = os.getenv("YD_API_KEY")


class DogAPI:
    API_BASE_URL = "https://dog.ceo/api/breed"

    def get_sub_breeds(self, bread: str) -> list[str]:
        try:
            response = requests.get(f"{self.API_BASE_URL}/{bread}/list")
            response.raise_for_status()
            return response.json()["message"]
        except requests.exceptions.RequestException as e:
            print("Ошибка при запросе к API", e)
            return []
        except KeyError as e:
            print("Ошибка при обработке ответа от API", e)
            return []


class YaDiskAPI:
    API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, token):
        self.token = token

    def create_folder(self, name_folder):
        try:
            headers = {"Authorization": f"OAuth {self.token}"}
            params = {"path": f"disk:/{name_folder}"}
            response = requests.put(self.API_BASE_URL, params=params, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Ошибка при создании папки", e)


if __name__ == "__main__":
    pass
