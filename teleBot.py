import telegram as tg
import requests


class teleBot:
    token = ''
    api = ''


def init(key, secret, api):


def notify(channel, message):
    try:
        response = requests.post(
            apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
