from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table, func

from database import Base

comment_likes = Table(
    "comment_likes",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True),
    Column("comment_id", Integer, ForeignKey("comments.comment_id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    )