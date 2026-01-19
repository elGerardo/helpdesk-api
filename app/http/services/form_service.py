from app.http.dtos.forms.store_form_dto import StoreFormDTO
from app.models.form import Form
from config.database import get_session

class FormService:
    @staticmethod
    async def store(dto: StoreFormDTO, session=None) -> Form:
        if session is None:
            session = next(get_session())

        form = Form(
            tenant_id=dto.tenant_id,
            form_id=dto.form_id,
            board_id=dto.board_id,
            title=dto.title,
            nomenclature=dto.nomenclature,
            description=dto.description,
            status=dto.status,
            version=dto.version,
            created_by=dto.created_by
        )
        session.add(form)
        session.flush()

        return form
