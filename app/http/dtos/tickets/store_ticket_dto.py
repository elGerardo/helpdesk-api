from pydantic import BaseModel
from typing import Optional

class StoreTicketDTO(BaseModel):
    tenant_id: int
    workspace_id: int
    board_id: int
    form_id: int
    requester_name: str
    requester_mail: Optional[str] = None
    status: Optional[str] = None
