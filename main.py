from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/{file}")
async def root(request: Request, file: str):
    code = (Path.cwd() / file).read_text()
    return templates.TemplateResponse("index.html", {"request": request, "code": code})

