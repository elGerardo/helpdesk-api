from app.http.dtos.board_statuses.store_board_status_dto import StoreBoardStatusDTO
from app.models.board_status import BoardStatus
from config.database import get_session

class BoardStatusService:
    @staticmethod
    async def store(dto: StoreBoardStatusDTO, session=None) -> BoardStatus:
        if session is None:
            session = next(get_session())

        board_status = BoardStatus(
            tenant_id=dto.tenant_id,
            board_id=dto.board_id,
            label=dto.label,
            slug=dto.slug,
            type=dto.type
        )
        session.add(board_status)
        session.flush()

        return board_status
