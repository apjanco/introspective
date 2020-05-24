from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

# ALLOWED_HOSTS in Django settings.py
origins = [
    "http://localhost:8000",
]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/{file}")
async def root(request: Request, file: str):
    code = (Path.cwd() / file).read_text()
    return templates.TemplateResponse("index.html", {"request": request, "code": code})


@app.post("/change")
async def change_code(request: Request):
    data = await request.json()
    code = data["code"]
    filename = data["filename"]
    (Path.cwd() / filename).write_text(code)


