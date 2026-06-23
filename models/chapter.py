from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String, ForeignKey, func
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
if TYPE_CHECKING:
    from models.comment import Comment
    from models.novel import Novel

class Chapter(Base):
    __tablename__ = "chapters"
    chapter_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)
    chapter_number: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    
    
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.novel_id", ondelete="CASCADE"), nullable=False)
    novel: Mapped["Novel"] = relationship("Novel", back_populates="chapters")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="commented_chapter", cascade="all, delete-orphan")