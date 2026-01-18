from app.models.user import User
from config.database import get_session
from config.app import HASH
from app.http.services.tenant_service import TenantService
from app.http.services.workspace_service import WorkspaceService
from app.http.services.user_workspace_service import UserWorkspaceService
from app.http.services.notification_service import NotificationService
from app.http.dtos.tenants.store_tenant_dto import StoreTenantDTO
from app.http.dtos.workspaces.store_workspace_dto import StoreWorkspaceDTO
from app.http.dtos.user_workspaces.store_user_workspace_dto import StoreUserWorkspaceDTO
from faker import Faker

class GuestService:

    async def store() -> User:
        session = next(get_session())

        # Create tenant with fake data 
        tenant = await TenantService.store(
            StoreTenantDTO(
                owner_id=None,
                title=Faker().company(),
                description=Faker().catch_phrase()
            ),
            session=session
        )

        fakeName = Faker().user_name().capitalize()
        fakeLastName = Faker().last_name().capitalize()
        
        # Create user with fake data
        user = User(
            tenant_id=tenant.id,
            name=fakeName,
            last_name=fakeLastName,
            user_name=f'{fakeName.lower()}_{fakeLastName.lower()}_{Faker().random_number(digits=3)}',
            email=f'{fakeName.lower()}_{fakeLastName.lower()}@example.com',
            password=HASH.hash('12345')
        )
        session.add(user)
        session.flush()
        
        tenant.owner_id = user.id

        # Create second user with fake data
        fakeName = Faker().user_name().capitalize()
        fakeLastName = Faker().last_name().capitalize()
        second_user = User(
            tenant_id=tenant.id,
            name=fakeName,
            last_name=fakeLastName,
            user_name=f'{fakeName.lower()}_{fakeLastName.lower()}_{Faker().random_number(digits=3)}',
            email=f'{fakeName.lower()}_{fakeLastName.lower()}@example.com',
            password=HASH.hash('12345')
        )
        session.add(second_user)
        session.flush()
        
        # Create workspace with fake data
        faker = Faker()
        workspace = await WorkspaceService.store(
            StoreWorkspaceDTO(
                tenant_id=tenant.id,
                name=faker.bs().title(),
                description=faker.catch_phrase(),
                logo=None,
                color=faker.hex_color()
            ),
            session=session
        )
        
        await UserWorkspaceService.store(
            StoreUserWorkspaceDTO(
                user_id=user.id,
                workspace_id=workspace.id,
                tenant_id=tenant.id
            ),
            session=session
        )
        
        # Create notification
        await NotificationService.store(
            row=1,
            table="tickets",
            generated_by=second_user.id,
            deliveried_to=user.id,
            meta={
                "title": "New ticket assigned",
                "text": "Ticket #1 has been assigned to you"
            },
            session=session
        )
        
        session.commit()
        session.refresh(user)

        return user