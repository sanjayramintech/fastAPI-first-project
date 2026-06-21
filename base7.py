from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello"

@app.get("/student")
def student(name: str):
    return f"hello {name}"


@app.get("/add")
def add(a: int, b: int):
    c=a + b
    return f"{c} is the sum"

@app.get("/multiply")
def multiply(a: int,b: int):
    c=a*b
    return f"{c} is the product"
    