from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_home():
    return "This is GET"

@app.post("/")
def post_home():
    return "This is POST"