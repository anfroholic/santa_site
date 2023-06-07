import uvicorn

from fastapi import FastAPI

from fastapi.responses import HTMLResponse



# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()
app = FastAPI()
       

@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    print("there's a new cowboy in town!!")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return f"""
    <h1>Santa Site for Mark Wingate</h1>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")
