from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

friends = ["Ram", "Arun", "Sanjay", "Akhil"]

@app.get("/", response_class=HTMLResponse)
def home():
    chosen = random.choice(friends)

    return f"""
    <html>
        <head>
            <title>Tea Picker</title>
        </head>
        <body>
            <h1>☕ Tea Picker</h1>
            <h2>Today's tea buyer is:</h2>
            <h1>{chosen}</h1>
        </body>
    </html>
    """