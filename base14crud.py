from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.post("/student")
def create_student(stu: Student):
    return stu

@app.get("/student/{id}")
def get_student(id: int):
    return {"id": id}

@app.put("/student/{id}")
def update_student(id: int, stu: Student):
    return {
        "id": id,
        "name": stu.name,
        "age": stu.age
    }

@app.delete("/student/{id}")
def delete_student(id: int):
    return {
        "message": f"Student {id} deleted"
    }