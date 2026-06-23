from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime
from sqlalchemy import func
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.chapter import Chapter
    from models.novel import Novel
    from models.user import User
class Comment(Base):
    __tablename__ = "comments"
    comment_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.novel_id", ondelete="CASCADE"), nullable=True)
    chapter_id: Mapped[int] = mapped_column(Integer, ForeignKey("chapters.chapter_id", ondelete="CASCADE"), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False) # The user which made the comment
    parent_comment_id: Mapped[int] = mapped_column(Integer, ForeignKey("comments.comment_id"), nullable=True) # The parent comment if this is a reply
    content: Mapped[str] = mapped_column(String, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    
    commenter: Mapped["User"] = relationship("User", back_populates="comments")
    commented_novel: Mapped["Novel"] = relationship("Novel", back_populates="comments")
    commented_chapter: Mapped["Chapter"] = relationship("Chapter", back_populates="comments")
    parent_comment: Mapped["Comment"] = relationship("Comment", remote_side=[comment_id], back_populates="replies")
    replies: Mapped[list["Comment"]] = relationship("Comment", back_populates="parent_comment")
    
    __table_args__ = (
    CheckConstraint(
    "(novel_id IS NOT NULL AND chapter_id IS NULL) OR "
    "(novel_id IS NULL AND chapter_id IS NOT NULL)",
    name="exactly_one_target")
        )