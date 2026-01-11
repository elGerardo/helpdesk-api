from starlette.responses import JSONResponse
from starlette.requests import Request
from app.http.services.user_workspace_service import UserWorkspaceService
from app.utils.http_status import ok

class UserWorkspacesController:

    async def index(request: Request) -> JSONResponse:
        result = await UserWorkspaceService.get_all(request.state.user)
        return ok(result)