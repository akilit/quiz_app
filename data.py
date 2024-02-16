import requests


def get_questions():
    url = "https://opentdb.com/api.php?amount=10"
    parameters = {
        "difficulty": "medium",
        "type": "boolean",
    }
    trivia = requests.get(url, params=parameters)
    return trivia.json()
