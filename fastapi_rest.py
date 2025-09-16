from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from pydantic import BaseModel
import pybase64
import time

# https://fastapi.tiangolo.com/de/tutorial/


# Optional: Cyclic routine
scheduler = BackgroundScheduler()
def cyclic():
    print(f"Cyclic task at {time.strftime('%X')}")


# Optional: Routine to initialize and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing..")
    scheduler.add_job(cyclic, "interval", seconds=10)  # run every 10s
    scheduler.start()

    yield  # App runs while paused here

    scheduler.shutdown()
    print("Shutdown..")


app = FastAPI(lifespan=lifespan)


## Simple JSON datatype
class Json(BaseModel):
    text1: str
    text2: str


@app.post("/json/")
def json_input(json: Json):
    return {"message": "Json received", "content": json}
# Linux:   curl -X POST "http://localhost:8080/json/" -H "Content-Type: application/json" -d '{"text1": "Hello", "text2": "World!"}'
# Windows: curl -X POST "http://localhost:8080/json/" -H "Content-Type: application/json" -d "{""text1"": ""Hello"", ""text2"": ""World!""}"


@app.get("/json/")
async def json_output():
    return {"message": "Hello World!"}
# curl -X GET "http://localhost:8080/json/"


## Handle Base64 data
@app.post("/base64/")
async def base64_input(base64: Request):
    body = await base64.body()
    text = body.decode("utf-8")
    return {"message": "Base64 received", "content": text, "decoded": pybase64.standard_b64decode(text)}


@app.get("/base64/")
async def base64_output():
    return {"message": pybase64.standard_b64encode(b'Hello World!')}
# curl -X POST "http://localhost:8080/base64/" -H "Content-Type: text/plain" -d "SGVsbG8gV29ybGQh"
