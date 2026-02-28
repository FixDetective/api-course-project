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


if __name__ == "__main__":
    pass