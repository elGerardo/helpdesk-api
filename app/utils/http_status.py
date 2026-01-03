from starlette.responses import JSONResponse

def created(data: dict):
    return JSONResponse(data, status_code=201)

def updated(data: dict):
    return JSONResponse(data, status_code=202)

def ok(data: dict):
    return JSONResponse(data, status_code=200)

def deleted():
    return JSONResponse(status_code=204)