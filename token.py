import requests
from onelogin_config import client_id, client_secret

def generateToken():
    r = requests.post(token_url, auth=(client_id, client_secret), json={"grant_type": "client_credentials"})
    bearer_token = r.json()['access_token']
    print('new token = ', bearer_token)
    return bearer_token

token = generateToken()
