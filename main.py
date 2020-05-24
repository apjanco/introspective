from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
#i
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    code = (Path.cwd() / "main.py").read_text()
    return templates.TemplateResponse("index.html", {"request": request, "code": code})


@app.post("/change")
async def change_code(request: Request):
    data = 'TODO'
    (Path.cwd() / "main.py").write_text(data)













