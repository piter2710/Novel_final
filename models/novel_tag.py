from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

novel_tags = Table(
    "novel_tag",
    Base.metadata,
    Column("novel_id", Integer, ForeignKey("novels.novel_id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.tag_id"), primary_key=True)
)