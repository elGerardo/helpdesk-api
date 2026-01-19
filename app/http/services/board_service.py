from app.http.dtos.boards.store_board_dto import StoreBoardDTO
from app.models.board import Board
from config.database import get_session

class BoardService:
    @staticmethod
    async def store(dto: StoreBoardDTO, session=None) -> Board:
        if session is None:
            session = next(get_session())

        board = Board(
            tenant_id=dto.tenant_id,
            workspace_id=dto.workspace_id,
            name=dto.name,
            nomenclature=dto.nomenclature,
            description=dto.description,
            logo=dto.logo
        )
        session.add(board)
        session.flush()

        return board
