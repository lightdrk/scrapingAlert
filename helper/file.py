import configparser
import requests
import json

def readfiles():
    config = configparser.ConfigParser()
    config.read('./config.ini')

    chat_id = config['app']['chat_id']
    token = config['app']['token']
    return chat_id, token

def createFile(token):
    config = configparser.ConfigParser()
    response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates', timeout=10)
    json_object = json.loads(response.text)
    chat_id = json_object["result"][0]["message"]["chat"]["id"]
    config.add_section('app')
    config.set('app', 'chat_id', f'{chat_id}')
    config.set('app', 'token', f'{token}')
    with open('config.ini','w') as configfile:
        config.write(configfile)
