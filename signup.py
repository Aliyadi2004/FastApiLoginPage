from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from Operation import main
mainUI = main()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("sinup.html", {"request": request})
    
@app.post("/signup")
async def submit_form(username: str = Form(...), password: str = Form(...), Rep_password: str = Form(...)):
    print(username, password , Rep_password)
    if Rep_password != password:
        return HTMLResponse(content="<p>Invalid username or password</p>")
    else:
        mainUI.sinup(username, password)
        return HTMLResponse(content=f"<p>Mr. {username},You are in.</p>")
  