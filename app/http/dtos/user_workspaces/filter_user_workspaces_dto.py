from pydantic import BaseModel, Field

class FilterUserWorkspacesDto(BaseModel):
    limit: int = Field(default=10, gt=0) #gt means greater than
    page: int = Field(default=0)
