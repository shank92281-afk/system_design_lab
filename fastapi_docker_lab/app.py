from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from db import async_session

app = FastAPI()

# Link FastAPI to your templates folder
templates = Jinja2Templates(directory="templates")

# Serve your HTML page at "/"
@app.get("/", response_class=HTMLResponse)
async def serve_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Handle form submission and save data in DB
@app.post("/users")
async def add_user(name: str, email: str):
    async with async_session() as session:
        await session.execute(
            text("INSERT INTO users (name, email) VALUES (:name, :email)"),
            {"name": name, "email": email}
        )
        await session.commit()
    return {"message": "✅ User added successfully!"}

