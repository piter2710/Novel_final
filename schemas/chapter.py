from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ChapterBase(BaseModel):
    title: str
    content: str | None = None
    chapter_number: int
    
class ChapterCreate(ChapterBase):
    pass

class ChapterOut(ChapterBase):
    chapter_id: int
    novel_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
class ChapterUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
