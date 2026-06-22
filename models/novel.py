from sqlalchemy import Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
class Novel(Base):
    __tablename__ = "novels"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
