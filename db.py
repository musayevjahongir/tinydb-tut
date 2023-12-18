from tinydb import TinyDB
from tinydb.database import Document


db = TinyDB('db.json', indent=4)

users = db.table(name='users')

# print(users.all())
print(users.get(doc_id=31))