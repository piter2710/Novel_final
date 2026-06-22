from sqlalchemy import Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)