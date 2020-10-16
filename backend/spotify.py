import requests
import json
import base64

CLIENT_ID = "f43cf4e8036f45c6b453e23b7bc01ccc"
CLIENT_SECRET = "691624db96c14368ac34af9c5d718044"


def get_token():
    code_payload = {
        'grant_type': 'client_credentials'
    }

    auth_str = '{}:{}'.format(CLIENT_ID, CLIENT_SECRET)
    b64_auth_str = base64.urlsafe_b64encode(auth_str.encode()).decode()

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(b64_auth_str)
    }

    URL = "https://accounts.spotify.com/api/token"
    post_request = requests.post(URL, data=code_payload, headers=headers)

    response_data = json.loads(post_request.text)

    return response_data['token_type'] + " " + response_data['access_token']
