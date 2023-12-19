from tinydb import TinyDB
import requests

def user():

    response=requests.get('https://randomuser.me/api/').json()
    return response["results"][0]


db = TinyDB('db.json', indent=4)

male = db.table(name='male')
female=db.table(name="female")

while True:
    users=user()
    if users['gender']=="male":
        if len(male)<=30:
            male.insert(users)
    elif users['gender']=="female":
        if len(female)<=30:
            female.insert(users)
        else:
            break


