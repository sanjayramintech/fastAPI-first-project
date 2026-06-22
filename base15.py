from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary database
students = []

# Model
class Student(BaseModel):
    name: str
    age: int


# Create a student
@app.post("/student")
def create_student(stu: Student):
    students.append(stu)
    return {
        "message": "Student added successfully"
    }


# Get all students
@app.get("/students")
def get_students():
    return students


# Get one student by index
@app.get("/student/{index}")
def get_student(index: int):
    return students[index]


# Update a student
@app.put("/student/{index}")
def update_student(index: int, stu: Student):
    students[index] = stu
    return {
        "message": "Student updated",
        "student": stu
    }


# Delete a student
@app.delete("/student/{index}")
def delete_student(index: int):
    deleted_student = students.pop(index)
    return {
        "message": "Student deleted",
        "student": deleted_student
    }