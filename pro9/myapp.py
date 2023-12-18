import requests
import json

URL="http://127.0.0.1:8000/stuapi/"

def get_data(id = None ):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data =r.json()
    print(data)
get_data() 
    
def post_data():
    data={
        'name':'kamini',
        'roll':21,
        'city':'mumbai'
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data =r.json()
    print(data)
# post_data()

def update_data():
    data={
        'id':4,
        'name':'radhika',
        'roll':15,
        'city':'goa'
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data =r.json()
    print(data)
# update_data()
    
def delete_data():
    data={'id':'2' }

    json_data=json.dumps(data)
    headers={'content-type':'application/json'}

    r=requests.delete(url=URL,headers=headers,data=json_data)
    data =r.json()
    print(data)
# delete_data()