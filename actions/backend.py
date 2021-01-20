import requests
import random

search_api = "http://newsapi.org/v2/everything?apiKey=05014df9b6474b9fba0aeb70e1b7a161&q={}&language=en&pageSize=1&page=5"
word_api = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

def fetch_actions():
    return {
        "text": "Choose what action you want to do?",
        "list": [
            {"title": "Fetch Random Integer", "id": 1},
            {"title": "Fetch Article", "id": 2}
        ]
    }

def fetch_random_number():
    return random.random()

def fetch_article(article="Chatbot"):
    result = requests.get(search_api.format(article)).json()
    try:
        return [
            {"url": data['url'], "title": data['title'], "description": data['description']} for data in result['articles'][0]
        ]
    except:
        return []

def fetch_word_meaning(word="chatbot"):
    try:
        result = requests.get(word_api.format(word))
        return result.json()
    except:
        return []

