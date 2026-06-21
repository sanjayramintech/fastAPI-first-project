from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello"

@app.get("/student/{name}")
def student(name: str):
    return f"hello {name}"
