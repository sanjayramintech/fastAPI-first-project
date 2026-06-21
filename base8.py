
from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
def hello():
    return "POST received"