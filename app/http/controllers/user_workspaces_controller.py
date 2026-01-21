from starlette.responses import JSONResponse
from starlette.requests import Request
from app.http.services.user_workspace_service import UserWorkspaceService
from app.http.dtos.user_workspaces.filter_user_workspaces_dto import FilterUserWorkspacesDto
from app.utils.http_status import ok

class UserWorkspacesController:

    async def index(request: Request) -> JSONResponse:
        query_params = FilterUserWorkspacesDto(**request.query_params)
        result = await UserWorkspaceService.get_all(request.state.user, query_params)
        return ok(result)