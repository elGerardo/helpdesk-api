from starlette.applications import Starlette
from app.routes.api import routes
from app.http.exceptions.validation_exception import validation_handler
from app.http.middleware.json_validation_middleware import JSONValidationMiddleware
from pydantic import ValidationError
from config import app

app = Starlette(
    debug=app.DEBUG, 
    routes=routes, 
    exception_handlers={
        ValidationError: validation_handler
    }
)

app.add_middleware(JSONValidationMiddleware)

@app.on_event("startup")
async def startup():
    """Startup app."""