from typing import TypedDict

class Students(TypedDict):
    name: str
    age: int

person: Students = {'name':'MANI','age':'24'}

print(person)