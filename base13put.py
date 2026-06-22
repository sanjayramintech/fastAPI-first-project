from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.put("/student/{id}")
def update_student(id: int, stu: Student):
    return {
        "student_id": id,
        "name": stu.name,
        "age": stu.age,
        "message": "Student updated"
    }