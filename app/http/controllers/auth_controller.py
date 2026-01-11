from starlette.requests import Request 
from app.http.dtos.auth.login_dto import LoginDTO
from app.utils.http_status import created, ok
from starlette.responses import JSONResponse
from app.http.services.auth_service import AuthService

class AuthController:

    async def login(request: Request) -> JSONResponse:
        payload = request.state.body
            
        dto = LoginDTO.model_validate(payload)
        result = await AuthService.login(dto)

        if "error" in result:
            return JSONResponse({
                "error": result["error"]
            }, status_code=401)

        return created(result)

    async def me(request: Request) -> JSONResponse:
        token = request.headers.get("Authorization")
        user = await AuthService.me(token)
        return ok(user) 