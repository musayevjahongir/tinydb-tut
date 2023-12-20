from tinydb import TinyDB, Query
from tinydb.database import Document
from randomusers import get_users_by_gender


db = TinyDB('db.json', indent=4)

males = db.table('males')
females = db.table('females')


q = Query()

fields = {
    "age": 17
}

print(males.count(cond=q.country == 'Brazil'))
