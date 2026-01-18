from app.models.notification import Notification
from config.database import get_session
from typing import Optional
from datetime import datetime

class NotificationService:
    
    async def store(
        row: int,
        table: str,
        generated_by: int,
        deliveried_to: int,
        meta: Optional[dict] = None,
        session=None
    ) -> Notification:
        """Store a new notification row."""
        if session is None:
            session = next(get_session())
        
        notification = Notification(
            row=row,
            table=table,
            generated_by=generated_by,
            deliveried_to=deliveried_to,
            meta=meta,
            is_seen=False,
            created_at=datetime.now()
        )
        
        session.add(notification)
        session.flush()
        
        return notification
