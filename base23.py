from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tiktoken

app = FastAPI()

# tokenizer
encoder = tiktoken.get_encoding("cl100k_base")

# storage
texts = []

# request model
class TextInput(BaseModel):
    text: str


# CREATE
@app.post("/texts")
def create_text(data: TextInput):

    token_count = len(encoder.encode(data.text))

    cost = token_count * 0.000002

    sample = {
        "id": len(texts) + 1,
        "text": data.text,
        "tokens": token_count,
        "cost": cost
    }

    texts.append(sample)

    return sample


# READ ALL
@app.get("/texts")
def get_all():
    return texts


# READ ONE
@app.get("/texts/{id}")
def get_one(id: int):

    for sample in texts:
        if sample["id"] == id:
            return sample

    raise HTTPException(
        status_code=404,
        detail="Text sample not found"
    )


# UPDATE
@app.put("/texts/{id}")
def update_text(id: int, data: TextInput):

    for sample in texts:

        if sample["id"] == id:

            token_count = len(
                encoder.encode(data.text)
            )

            cost = token_count * 0.000002

            sample["text"] = data.text
            sample["tokens"] = token_count
            sample["cost"] = cost

            return sample

    raise HTTPException(
        status_code=404,
        detail="Text sample not found"
    )


# DELETE
@app.delete("/texts/{id}")
def delete_text(id: int):

    for sample in texts:

        if sample["id"] == id:
            texts.remove(sample)

            return {
                "message": "Deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Text sample not found"
    )