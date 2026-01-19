from app.models.user import User
from config.database import get_session
from config.app import HASH
from app.http.services.tenant_service import TenantService
from app.http.services.workspace_service import WorkspaceService
from app.http.services.user_workspace_service import UserWorkspaceService
from app.http.services.notification_service import NotificationService
from app.http.services.ticket_service import TicketService
from app.http.services.ticket_responsible_service import TicketResponsibleService
from app.http.services.board_service import BoardService
from app.http.services.board_status_service import BoardStatusService
from app.http.services.user_board_service import UserBoardService
from app.http.services.form_service import FormService
from app.http.dtos.tenants.store_tenant_dto import StoreTenantDTO
from app.http.dtos.workspaces.store_workspace_dto import StoreWorkspaceDTO
from app.http.dtos.user_workspaces.store_user_workspace_dto import StoreUserWorkspaceDTO
from app.http.dtos.tickets.store_ticket_dto import StoreTicketDTO
from app.http.dtos.boards.store_board_dto import StoreBoardDTO
from app.http.dtos.board_statuses.store_board_status_dto import StoreBoardStatusDTO
from app.http.dtos.forms.store_form_dto import StoreFormDTO
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
        
        # Create board
        board = await BoardService.store(
            StoreBoardDTO(
                tenant_id=tenant.id,
                workspace_id=workspace.id,
                name=faker.catch_phrase(),
                nomenclature=faker.word().upper(),
                description=faker.text(max_nb_chars=50)
            ),
            session=session
        )
        
        await UserBoardService.store(
            user_id=user.id,
            workspace_id=workspace.id,
            board_id=board.id,
            tenant_id=tenant.id,
            session=session
        )
        
        await UserBoardService.store(
            user_id=second_user.id,
            workspace_id=workspace.id,
            board_id=board.id,
            tenant_id=tenant.id,
            session=session
        )
        
        # Create board statuses
        status_open = await BoardStatusService.store(
            StoreBoardStatusDTO(
                tenant_id=tenant.id,
                board_id=board.id,
                label="Open",
                slug=f"{board.id}-OPEN",
                type="DEFAULT"
            ),
            session=session
        )
        
        status_closed = await BoardStatusService.store(
            StoreBoardStatusDTO(
                tenant_id=tenant.id,
                board_id=board.id,
                label="Closed",
                slug=f"{board.id}-CLOSED",
                type="DEFAULT"
            ),
            session=session
        )
        
        form_title = faker.catch_phrase()
        form = await FormService.store(
            StoreFormDTO(
                tenant_id=tenant.id,
                form_id=None,
                board_id=board.id,
                title=form_title,
                nomenclature=form_title[:2].upper(),
                description=faker.text(max_nb_chars=100),
                status="PUBLISHED",
                version=1,
                created_by=user.id
            ),
            session=session
        )
        
        # Create two tickets with required data
        ticket1 = await TicketService.store(
            StoreTicketDTO(
                tenant_id=tenant.id,
                workspace_id=workspace.id,
                board_id=board.id,
                form_id=form.id,
                requester_name=faker.name(),
                status=status_open.slug
            ),
            session=session
        )
        
        ticket2 = await TicketService.store(
            StoreTicketDTO(
                tenant_id=tenant.id,
                workspace_id=workspace.id,
                board_id=board.id,
                form_id=form.id,
                requester_name=faker.name(),
                status=status_open.slug
            ),
            session=session
        )
        
        await TicketResponsibleService.store(
            user_id=user.id,
            ticket_id=ticket1.id,
            tenant_id=tenant.id,
            session=session
        )
        
        await TicketResponsibleService.store(
            user_id=user.id,
            ticket_id=ticket2.id,
            tenant_id=tenant.id,
            session=session
        )
        
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