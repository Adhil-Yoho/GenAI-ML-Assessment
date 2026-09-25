
import requests
import json


class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout

    def get_data(self, endpoint: str = "") -> dict:
        url = self.base_url + endpoint
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            print(f"API call successful. Status code: {response.status_code}")
            return data

        except requests.exceptions.Timeout:
            print("API call timed out. Continuing without API data")
            return {}

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")
            return {}

        except json.JSONDecodeError:
            print("Could not decode API response as JSON")
            return {}

    def save_cache(self, data:dict,path) -> None:
        with open(path,'w') as f:
            json.dump(data,f,indent =4)
        print(f'API data cached to {path}')
