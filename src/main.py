import uvicorn

from fastapi import FastAPI, Query

from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime
from fastapi import FastAPI, Form, Request, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.choose_adventure import story, lookup, adventures

import io, json
# import debugpy
hostname='santamark4xmas.com'
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()
app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static", html=True), name="static")
templates = Jinja2Templates(directory='src/htmldirectory')    

# @app.on_event("startup")
# async def startup_event():
#     """Start up event for FastAPI application."""

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'hostname': hostname})

@app.get("/booking", response_class=HTMLResponse)
async def calendar(request: Request):
    return templates.TemplateResponse('booking.html', {'request': request, 'hostname': hostname})

@app.get("/choose_adventure", response_class=HTMLResponse)
async def choose_adventure(request: Request):
    return templates.TemplateResponse('choose_adventure.html', {'request': request, 'story': story, 'lookup': list(lookup.keys())})

@app.post("/adventure", response_class=HTMLResponse)
async def choose_adventure(request: Request):
    def get_snip(chapter, name):
        for option in chapter:
            if option['name'] == name:
                return option['snippet']
            
    raw = dict(await request.form())
    
    # with open('temp.json', 'w') as f:
    #     json.dump(raw, f, indent=2)
        
    # with open('temp.json', 'r') as f:
    #     pretty = f.read()
        
    # print(pretty)
    print(raw)
    
    adventure = {k:v for k,v in raw.items() if '|' not in k} 
    for k, v in adventure.items():
        if v == "Special Request":
            adventure[k] = f"Special Request: {raw[f'{k}|Special Request']}"
            
    
    print(adventure)
    full_text = []
    for k,v in adventure.items():
        if 'Special Request: ' not in v:
            if k == 'family':
                full_text.append(v)
                continue
            
            chapter = story[k]
            snip = get_snip(chapter=chapter, name=v)
            
            full_text.append(snip)
        
        else:
            remove = len('Special Request: ')
            text = v[remove:].split('\n')
            full_text.extend(text)
       
    return templates.TemplateResponse('adventure.html', {'request': request, 'adventure': adventure, 'full_text': full_text})

@app.get("/get_adventures", response_class=JSONResponse)
async def get_adventures(request: Request):
    cutlist = []
    for adventure in adventures:
        if adventure['Greeting'].startswith('Special Request: '):
            greeting = adventure['Greeting'].replace('Special Request: ', '')
            
            cut = {
                'family': adventure['family'],
                'create_clip': greeting,
            }
            cutlist.append(cut)
            
    return {
        'cutlist': cutlist,
        'adventures': adventures
    }



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