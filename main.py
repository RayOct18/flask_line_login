from flask import Flask, redirect, request
from furl import furl
import requests
import json
import jwt
import pickle

from decode_id_token import decode_id_token


app = Flask(__name__)

client_id = 'Channel ID'
client_secret = 'Channel secret'

@app.route('/')
def index():
    url = 'https://access.line.me/oauth2/v2.1/authorize'
    param = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': 'http://127.0.0.1:5001/auth/callback',
        'state': 'random',
        'scope': 'openid profile'
        }
    url = str(furl(url).set(param))
    return redirect(url, 302)

@app.route('/auth/callback', methods=['GET', 'POST'])
def callback():
    code = request.args.get('code')
    access_token_url = 'https://api.line.me/oauth2/v2.1/token'
    param = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': 'http://127.0.0.1:5001/auth/callback',
        }

    r = requests.post(access_token_url, data=param)
    data = json.loads(r.text)
    access_token = data.get('access_token')
    id_token = data.get('id_token')

    with open('test_token.pickle', 'wb') as token:
        pickle.dump({'id_token': id_token, 'access_token': access_token}, token)

    payload_json = decode_id_token(id_token, client_id, client_secret)
    payload_json.update(data)

    return payload_json


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
