# imports

import requests

TRIVIA_API = "https://opentdb.com/api.php"
API_PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(TRIVIA_API, API_PARAMETERS)
response.raise_for_status()

question_data = response.json()["results"]

