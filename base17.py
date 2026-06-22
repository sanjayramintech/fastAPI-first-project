from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()
users=[]

class User(BaseModel):
    name:str
    pwd:int

class response(BaseModel):
    namem:str

@app.get("/user_info",status_code=200)
def info():
    return users

@app.get("/user_inf/{index}",status_code=200,response_model=response)
def infoorm(index: int):
    return users[index]



@app.post("/creating",status_code=201)
def create_user(user:User):
    users.append(user)
    return {
        "message": "User created successfully",
        "user": user
    }