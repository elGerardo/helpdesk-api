from app.models.user_board import UserBoard
from config.database import get_session

class UserBoardService:
    @staticmethod
    async def store(user_id: int, workspace_id: int, board_id: int, tenant_id: int, session=None) -> UserBoard:
        if session is None:
            session = next(get_session())

        user_board = UserBoard(
            user_id=user_id,
            workspace_id=workspace_id,
            board_id=board_id,
            tenant_id=tenant_id
        )
        session.add(user_board)
        session.flush()

        return user_board
