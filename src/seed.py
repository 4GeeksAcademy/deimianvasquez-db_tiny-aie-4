from tinydb import TinyDB
from pydantic import BaseModel

class UserModel(BaseModel):
    lastname: str
    email: str
    dni: str
    phone: str

db = TinyDB('example.json')

db.truncate()
db.drop_table("users")


seed_data = [
    {
        'lastname':'Deimian Vásquez',
        'email':'deimian@example.com',
        'dni':'12345678',
        'phone':'123-456-7890'
    },
    {
        'lastname':'Angel Tovar',
        'email':'angel@example.com',
        'dni':'87654321',
        'phone':'987-654-3210'
    },
    {
        'lastname':'Atilio Vásquez',
        'email':'atilio@example.com',
        'dni':'11223344',
        'phone':'111-222-3333'
    }
]

for user in seed_data:
    db.insert(UserModel(**user).model_dump())

print(f"Ingresados {len(seed_data)} registros")