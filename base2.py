from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

friends = ["Ram", "Shown", "Sanjay", "Akhil", "Aron"]

@app.get("/", response_class=HTMLResponse)
def home():
    chosen = random.choice(friends)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tea Picker</title>
        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
                color: white;
            }}

            .card {{
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                width: 400px;
            }}

            h1 {{
                font-size: 40px;
            }}

            h2 {{
                margin-top: 20px;
            }}

            .name {{
                font-size: 35px;
                color: #ffd700;
                margin: 20px 0;
            }}

            button {{
                padding: 15px 30px;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                cursor: pointer;
                background: #ff9800;
                color: white;
            }}

            button:hover {{
                transform: scale(1.05);
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>☕ Tea Picker</h1>

            <h2>Today's tea buyer is:</h2>

            <div class="name">
                {chosen}
            </div>

            <button onclick="window.location.reload()">
                Pick Again
            </button>
        </div>
    </body>
    </html>
    """