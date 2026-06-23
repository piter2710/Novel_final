from pydantic import BaseModel, ConfigDict
from datetime import datetime
from schemas.user import UserPublic
class CommentBase(BaseModel):
    content: str
class CommentCreate(CommentBase):
    novel_id: int | None = None
    chapter_id: int | None = None
    parent_comment_id: int | None = None
class CommentOut(CommentBase):
    comment_id: int
    
    created_at: datetime
    updated_at: datetime
    commenter: UserPublic
    
    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
class CommentUpdate(BaseModel):
    content: str | None = None
    