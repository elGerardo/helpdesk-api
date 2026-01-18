from app.http.dtos.tenants.store_tenant_dto import StoreTenantDTO
from app.models.tenant import Tenant
from config.database import get_session

class TenantService:
    async def store(dto: StoreTenantDTO, session=None) -> Tenant:
        if session is None:
            session = next(get_session())

        tenant = Tenant(
            owner_id=dto.owner_id,
            title=dto.title,
            description=dto.description
        )
        session.add(tenant)
        session.flush()

        return tenant