from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):

    name: str = 'rathore'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4)

student = {'name':'mani', 'age':'25', 'email':'mani@gmail.com', 'cgpa':'2'}

student = Student(**student)

print(student)