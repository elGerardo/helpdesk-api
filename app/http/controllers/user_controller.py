from starlette.responses import JSONResponse
from starlette.requests import Request 
from config.database import get_session
from app.models.user import User
from app.http.dtos.users.store_user_dto import StoreUserDTO
from pydantic import ValidationError
from app.http.services.user_service import UserService
from app.utils.http_status import created

class UserController:

    async def store(request: Request) -> JSONResponse:
        try:
            payload = request.state.body
            
            user_data = StoreUserDTO.model_validate(payload)
            
            #session = next(get_session())
            #user = User(**payload).model_dump()
            #session.add(user)
            #session.commit()
            #session.refresh(user)
            
            return JSONResponse({}, status_code=201)
            
        except ValidationError as e:
            errors = [
                {
                    "field": ".".join(str(loc) for loc in error["loc"]),
                    "message": error["msg"],
                    "type": error["type"]
                }
                for error in e.errors()
            ]
            return JSONResponse({
                "error": "Validation error",
                "details": errors
            }, status_code=422)
            
        except Exception as e:
            return JSONResponse({
                "error": "Internal server error",
                "message": str(e)
            }, status_code=500)
        
    async def findOrStore(request: Request) -> JSONResponse:
        user_name = request.path_params.get('user_name')
        result = await UserService.find_or_store(user_name)
        return created(result.model_dump())