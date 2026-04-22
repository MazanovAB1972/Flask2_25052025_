from author import Author
from schema import AuthorSchema
json_data =  [
  {
    "id": 1,
    "name": "Alex",
    "email": "alex@mail.ru"
  },
  {
    "id": 2,
    "name": "Ivan",
    "email": "ivan@mail.ru"
  },
  {
    "id": 4,
    "name": "Tom",
    "email": "tom@mail.ru"
  }
]



schema = AuthorSchema(many=True)
result = schema.load(json_data)
print(result)