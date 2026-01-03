from pydantic import ValidationError
from starlette.responses import JSONResponse

async def validation_handler(request, exc: ValidationError):
    errors = [
        {
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        }
        for error in exc.errors()
    ]
    return JSONResponse(
        {"error": "Validation error", "details": errors},
        status_code=422
    )