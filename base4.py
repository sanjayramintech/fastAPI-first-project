from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return "hi monea dinesha"

