from sqlmodel import SQLModel
from starlette.responses import JSONResponse

def created(data: dict | SQLModel):
    if isinstance(data, SQLModel):
        data = data.model_dump()
    return JSONResponse(data, status_code=201)

def updated(data: dict | SQLModel):
    if isinstance(data, SQLModel):
        data = data.model_dump()
    return JSONResponse(data, status_code=202)

def ok(data: dict | SQLModel):
    if isinstance(data, SQLModel):
        data = data.model_dump()
    return JSONResponse(data, status_code=200)

def deleted():
    return JSONResponse(status_code=204)