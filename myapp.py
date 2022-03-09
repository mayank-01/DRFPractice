import requests
import json
URL = 'http://127.0.0.1:8000/stuapi2/'

def get_data(id=None):
    data = {}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Alen',
        'roll': 102,
        'city': 'Delhi'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,  data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 2,
        'name': 'Sudhanshu',
        'roll': 102,
        'city': 'Mandi Gobindgarh'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

get_data(2)