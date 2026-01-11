from app.http.dtos.workspaces.store_workspace_dto import StoreWorkspaceDTO
from app.models.workspace import Workspace
from config.database import get_session


class WorkspaceService:
    @staticmethod
    async def store(dto: StoreWorkspaceDTO, session=None) -> Workspace:
        if session is None:
            session = next(get_session())

        workspace = Workspace(
            tenant_id=dto.tenant_id,
            name=dto.name,
            description=dto.description,
            logo=dto.logo,
            color=dto.color
        )
        session.add(workspace)
        session.flush()

        return workspace
