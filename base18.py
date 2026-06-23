from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

samples = []

class TextSample(BaseModel):
    text: str

@app.post("/count")
def count_tokens(data: TextSample):
    tokens = len(data.text.split())
    cost = tokens * 0.00001

    return {
        "tokens": tokens,
        "cost": cost
    }

@app.post("/samples")
def create_sample(sample: TextSample):
    new_sample = {
        "id": len(samples) + 1,
        "text": sample.text
    }
    samples.append(new_sample)
    return new_sample

@app.get("/samples")
def get_samples():
    return samples

@app.get("/samples/{sample_id}")
def get_sample(sample_id: int):
    for sample in samples:
        if sample["id"] == sample_id:
            return sample
    raise HTTPException(status_code=404, detail="Sample not found")

@app.put("/samples/{sample_id}")
def update_sample(sample_id: int, sample: TextSample):
    for s in samples:
        if s["id"] == sample_id:
            s["text"] = sample.text
            return s
    raise HTTPException(status_code=404, detail="Sample not found")

@app.delete("/samples/{sample_id}")
def delete_sample(sample_id: int):
    for s in samples:
        if s["id"] == sample_id:
            samples.remove(s)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Sample not found")