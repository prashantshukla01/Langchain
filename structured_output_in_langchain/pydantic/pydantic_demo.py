#pydantic is a data validation and data parsing library for python
#it ensures that the data you work with is correct structured and type safe

from typing import Optional
from pydantic import BaseModel, EmailStr, Field 

class Student(BaseModel):
    name: str
    age : Optional[int] = None  #optional field
    email : EmailStr #special data type for email validation by pydantic
    cgpa: float = Field(gt=0 ,lt = 10 , default = 5, description='A decimal value representing the CGPA of the students')


new_student = {'name':'Prashant','age':'32', 'email':'prashant@gmail.com', 'cgpa':8.5}

student = Student(**new_student)  #data parsing

student_dict= dict(student)
print (student_dict['cgpa'])

student_json = student.model_dump_json()
print(student_json)




'''Pydantic LangChain me data validation ke liye use hota hai.
Ye LLM ke unstructured text output ko structured data me convert karta hai.
Pydantic schema define karta hai (fields, types, required values).
Galat format aane par validation error throw karta hai.
Type safety ensure karta hai (int, string, list etc.).
LangChain ke Tools aur Agents me input/output schema define karta hai.
JSON-like structured output nikalne me help karta hai.
Debugging aur error handling easy ho jati hai.
Production-level applications ke liye code ko reliable banata hai.
LLM pipelines ko clean, predictable aur maintainable banata hai.'''