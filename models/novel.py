from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, func
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


if TYPE_CHECKING:
    from models.review import Review
    from models.chapter import Chapter
    from models.comment import Comment
class Novel(Base):
    __tablename__ = "novels"
    novel_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    
    chapters: Mapped[list["Chapter"]] = relationship("Chapter", back_populates="novel", cascade="all, delete-orphan")
    comments: Mapped[list["Comment"]] = relationship("Comment", backref="novel", cascade="all, delete-orphan")
    reviews: Mapped[list["Review"]] = relationship("Review", backref="novel", cascade="all, delete-orphan")