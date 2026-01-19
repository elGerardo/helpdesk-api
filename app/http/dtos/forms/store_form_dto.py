from pydantic import BaseModel
from typing import Optional

class StoreFormDTO(BaseModel):
    tenant_id: int
    form_id: Optional[int] = None
    board_id: int
    title: str
    nomenclature: str
    description: Optional[str] = None
    status: str = "DRAFT"
    version: int = 1
    created_by: int
