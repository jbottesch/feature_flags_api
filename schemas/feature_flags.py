from datetime import datetime
from pydantic import BaseModel

class FeatureFlagsCreateSchema(BaseModel):
    name: str
    enabled: bool = True

class FeatureFlagsUpdateSchema(BaseModel):
    name: str | None = None
    enabled: bool | None = None

class FeatureFlagsReadSchema(BaseModel):
    id: int
    name: str
    enabled: bool
    created_at: datetime