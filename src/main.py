import uvicorn

from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from datetime import datetime
from fastapi import FastAPI, Form, Request, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# import debugpy

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

# def read_root():
#     return f"""
#     <h1>Santa Site for Mark Wingate</h1><br>
#     <strong>The current time is: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
#     """

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")
