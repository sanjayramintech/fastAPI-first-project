from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello"

@app.get("/name")
def name1():
    return "your name anime!"

@app.get("/place")
def place1():
    return "your place is palace!"



