from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    branch: str

@app.post("/admission")
def admission(student: Student):
    return {
        "message": "Admission Successful",
        "student": student
    }