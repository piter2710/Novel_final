from sqlalchemy import CheckConstraint, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import datetime
from sqlalchemy import func
class Comment(Base):
    __tablename__ = "comments"
    comment_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    #In code add logic that only one can be null, either novel_id or chapter_id to define where the comment is being made
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.id"), nullable=True)
    chapter_id: Mapped[int] = mapped_column(Integer, ForeignKey("chapters.id"), nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False) # The user which made the comment
    parent_comment_id: Mapped[int] = mapped_column(Integer, ForeignKey("comments.comment_id"), nullable=True) # The parent comment if this is a reply
    
    content: Mapped[str] = mapped_column(String, nullable=False)

    __table_args__ = (
    CheckConstraint(
        "NOT (novel_id IS NOT NULL AND chapter_id IS NOT NULL)",
        name="only_one_target"
    ),
    )