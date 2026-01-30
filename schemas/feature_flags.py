from datetime import datetime
from pydantic import BaseModel

class FeatureFlagCreateSchema(BaseModel):
    name: str
    enabled: bool = True

class FeatureFlagUpdateSchema(BaseModel):
    name: str | None = None
    enabled: bool | None = None

class FeatureFlagReadSchema(BaseModel):
    id: int
    name: str
    enabled: bool
    created_at: datetime

    class Config:
        from_attributes = True

