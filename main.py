import requests
import json
import pandas as pd
from config import *

def get_session()
    session = requests.Session()
    response = requests.request('GET', BASE_URL)
    return response


def generate_data():
    return df

def get_data(BASE_URL:str, headers:dict, food_item:str):
    params = {
        'query':food_item,
        'page' : 1
    }

    runner = True

    while runner:
        print(f'Running for {params.get('page')}')
        response = requests.request('GET', BASE_URL,headers= headers, params = params)

        if response.status_code <> 200:
            print(f'API returned code : {response.status_code} and Generated URL was {response.url}')
            return False

        if len(response.json()['items']) == 0:
            print(f'Reached to end for the {food_item}')
            return data


        for item in response.json()['items']:
            pass

        # Stopping after 15 pages (Force Stop in case of infinite loop)
        if page == 15: 
            print(f'Force stopping for {food_item}')
            runner = False

        page += 1

        params.update({'page':page})


    # if temp = response.json()


def transform():
    return df

def main():
    print('getting session')
    session_info = get_session()

    cookies = session.cookies

    header = {
        'Cookie': cookies.get('__cf_bm')
    }

    for food_item in food_items:


        data = get_data(BASE_URL, headers, food_item)

    



    return True


if __name__ == '__main__':
    print('Process Started')
    main()