from sqlalchemy import Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from models.novel import Novel

class Chapter(Base):
    __tablename__ = "chapters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    
    
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.id"), nullable=False)
    novel: Mapped["Novel"] = relationship("Novel", back_populates="chapters")