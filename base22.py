from pydantic import BaseModel
from fastapi import FastAPI
app=FastAPI()
class Text(BaseModel):
    text:str

@app.post("/count")
def count(text:Text):
    words = text.text.split()
    word_count = len(words)
    return {"word_count": word_count}
