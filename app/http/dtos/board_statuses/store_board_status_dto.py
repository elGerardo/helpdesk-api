from pydantic import BaseModel

class StoreBoardStatusDTO(BaseModel):
    tenant_id: int
    board_id: int
    label: str
    slug: str
    type: str
