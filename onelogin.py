import requests
import pandas as pd
import numpy as np
import json
from token import token

base_url = 'https://api.us.onelogin.com/api/1/'
page = 1

token_url = 'https://api.us.onelogin.com/auth/oauth2/v2/token'

def setKeys():
    headers = {"Authorization":"Bearer " + token}
    r = requests.get(base_url + 'users', headers=headers)
    dataframe = pd.DataFrame(columns=r.json()['data'][0].keys())
    return dataframe

users_df = setKeys()

def getNextPage(nextpage):
    global page
    page = page + 1
    print('PAGE ', page)
    headers = {"Authorization": "Bearer " + token}
    r = requests.get(nextpage, headers=headers)
    nextpage = r.json()['pagination']['next_link']
    users = r.json()['data']
    for user in users:
        s  = pd.Series(user,index=user.keys())
        global users_df
        users_df.loc[len(users_df)] = s
    users_df.to_csv('oneloginusers.csv')
    if nextpage:
        getNextPage(nextpage)

def getAllusers():
    headers = {"Authorization": "Bearer " + token}
    r = requests.get(base_url + 'users', headers=headers)
    nextpage = r.json()['pagination']['next_link']
    users_df = pd.DataFrame(columns=r.json()['data'][0].keys())
    if nextpage:
        getNextPage(nextpage)

getAllusers()
