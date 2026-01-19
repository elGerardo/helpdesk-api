from pydantic import BaseModel
from typing import Optional

class StoreBoardDTO(BaseModel):
    tenant_id: int
    workspace_id: int
    name: str
    nomenclature: str
    description: Optional[str] = None
    logo: Optional[str] = None
