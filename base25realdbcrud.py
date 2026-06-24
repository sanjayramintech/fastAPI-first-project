import sqlite3
import tiktoken

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Tokenizer
encoder = tiktoken.get_encoding("cl100k_base")

# Database connection
conn = sqlite3.connect("text.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS texts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    tokens INTEGER,
    cost REAL
)
""")

conn.commit()


# Pydantic model
class TextInput(BaseModel):
    text: str


# CREATE
@app.post("/texts")
def create_text(data: TextInput):

    tokens = len(encoder.encode(data.text))
    cost = tokens * 0.000002

    cursor.execute(
        """
        INSERT INTO texts(text, tokens, cost)
        VALUES (?, ?, ?)
        """,
        (data.text, tokens, cost)
    )

    conn.commit()

    return {
        "message": "Added successfully"
    }


# READ ALL
@app.get("/texts")
def get_all():

    cursor.execute("SELECT * FROM texts")

    return cursor.fetchall()


# READ ONE
@app.get("/texts/{id}")
def get_one(id: int):

    cursor.execute(
        "SELECT * FROM texts WHERE id=?",
        (id,)
    )

    row = cursor.fetchone()

    if row:
        return row

    raise HTTPException(
        status_code=404,
        detail="Text not found"
    )


# UPDATE
@app.put("/texts/{id}")
def update_text(id: int, data: TextInput):

    tokens = len(encoder.encode(data.text))
    cost = tokens * 0.000002

    cursor.execute(
        """
        UPDATE texts
        SET text=?, tokens=?, cost=?
        WHERE id=?
        """,
        (data.text, tokens, cost, id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Text not found"
        )

    return {"message": "Updated successfully"}


# DELETE
@app.delete("/texts/{id}")
def delete_text(id: int):

    cursor.execute(
        "DELETE FROM texts WHERE id=?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Text not found"
        )

    return {"message": "Deleted successfully"}