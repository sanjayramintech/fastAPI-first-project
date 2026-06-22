from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()

class Student(BaseModel):
    name: str
    age :int

@app.post("/login")
def create_student(stu : Student):
    return {
        f"HI  {stu.name}"+f"with age {stu.age}"
    }

