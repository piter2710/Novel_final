from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
class ReviewBase(BaseModel):
    rating: int = Field(ge=1, le=10, description="Rating must be between 1 and 10")
    comment: str | None = None

class ReviewCreate(ReviewBase):
    novel_id: int
class ReviewOut(ReviewBase):
    review_id: int
    novel_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
