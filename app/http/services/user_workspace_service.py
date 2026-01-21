from app.http.dtos.user_workspaces.store_user_workspace_dto import StoreUserWorkspaceDTO
from app.http.dtos.user_workspaces.filter_user_workspaces_dto import FilterUserWorkspacesDto
from app.models.user import User
from app.models.user_workspace import UserWorkspace
from app.models.workspace import Workspace
from config.database import get_session
from sqlmodel import select
from app.utils.query import get

class UserWorkspaceService:
    async def get_all(logged_user: User, filters: FilterUserWorkspacesDto, session=None) -> list[Workspace]:
        query = (
            select(Workspace)
            .join(UserWorkspace, Workspace.id == UserWorkspace.workspace_id)
            .where(UserWorkspace.user_id == logged_user.id)
            .where(UserWorkspace.tenant_id == logged_user.tenant_id)
        )
        
        result = await get(
            query=query, 
            fields_to_serialize=True,
            pagination={'page': filters.page, 'limit': filters.limit},
        )

        return result

    @staticmethod
    async def store(dto: StoreUserWorkspaceDTO, session=None) -> UserWorkspace:
        if session is None:
            session = next(get_session())

        user_workspace = UserWorkspace(
            user_id=dto.user_id,
            workspace_id=dto.workspace_id,
            tenant_id=dto.tenant_id
        )
        session.add(user_workspace)
        session.flush()

        return user_workspace
