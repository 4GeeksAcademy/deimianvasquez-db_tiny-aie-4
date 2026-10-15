from tinydb import TinyDB, Query
from pydantic import BaseModel


class UserModel(BaseModel):
    lastname: str
    email: str
    dni: str
    phone: str

db = TinyDB('example.json')


# try:
#     user = UserModel(
#         lastname='Deimian Vásquez',
#         email='deimian@example.com',
#         dni='12345678',
#         phone='123-456-7890'
#     )
#     db.insert(user.model_dump())
# except Exception as e:
#     print(f"Error creating user: {e}")


# {
#     'lastname':'Deimian Vásquez',
#     'email':'deimian@example.com',
#     'dni':'12345678',
#     'phone':'123-456-7890'
# }


# db.insert({
#    'lastname':'Atilio Vásquez',
#    'email':'atilio@example.com',
#    'dni':'11223344',
#    'phone':'111-222-3333'
# })

# db.insert_multiple([
#     {
#         'lastname':'Deimian Vásquez',
#         'email':'deimian@example.com',
#         'dni':'12345678',
#         'phone':'123-456-7890'
#     },
#     {
#         'lastname':'Angel Tovar',
#         'email':'angel@example.com',
#         'dni':'87654321',
#         'phone':'987-654-3210'
#     },
#     {
#         'lastname':'Atilio Vásquez',
#         'email':'atilio@example.com',
#         'dni':'11223344',
#         'phone':'111-222-3333'
#     }
# ])


# # users = list(map(lambda item: ({'id': item.doc_id,  **item}), db.all())) - metodo map
# users = [{'id': item.doc_id, **item} for item in db.all()] # list comprehensions


# for item in users:
#     print(item)

# print("*"*100)

# # user = db.get(doc_id=10)
# User = Query()
# user = db.search(User.email == 'deimian@example.com')
# # db.update({'email': 'carlos@example.com'}, doc_ids=[4])
# # user_delete = db.remove(User.email == 'deimian@example.com')
# print(user)
# # print(user_delete)



# table = db.table('users')
# table.insert(user.model_dump())