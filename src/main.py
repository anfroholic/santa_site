import uvicorn

from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from datetime import datetime
from fastapi import FastAPI, Form, Request, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# import debugpy
hostname='santamark4xmas.com'
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()
app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static", html=True), name="static")
templates = Jinja2Templates(directory='src/htmldirectory')    

@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    print("there's a new cowboy in town!!")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@app.get("/booking", response_class=HTMLResponse)
async def calendar(request: Request):
    return templates.TemplateResponse('booking.html', {'request': request})


pics = [
    'FB_IMG_1637615348424.jpg',
    'FB_IMG_1637615437607.jpg',
    'FB_IMG_1641144420291.jpg',
    'FB_IMG_1636497702106.jpg',
    'FB_IMG_1636497721456.jpg',
    'FB_IMG_1637373239319.jpg'
]


@app.get("/gallery", response_class=HTMLResponse)
async def calendar(request: Request):
    return templates.TemplateResponse('gallery.html', {'request': request, 'pics': pics, 'hostname': hostname})