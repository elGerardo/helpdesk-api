from starlette.applications import Starlette
from app.routes.api import routes
from app.http.exceptions.validation_exception import validation_handler
from pydantic import ValidationError
from config import app

app = Starlette(
    debug=app.DEBUG, 
    routes=routes, 
    exception_handlers={
        ValidationError: validation_handler
    }
)

@app.on_event("startup")
async def startup():
    """Startup app."""