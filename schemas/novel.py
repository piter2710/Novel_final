from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
class NovelBase(BaseModel):
    title: str
    description: str | None = None

class NovelCreate(NovelBase):
    pass

class NovelOut(NovelBase):
    novel_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
class NovelUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
