from sqlalchemy import CheckConstraint, Integer, String, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.novel import Novel
    from models.user import User
class Review(Base):
    __tablename__ = "reviews"
    review_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.novel_id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(String, nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    
    
    novel: Mapped["Novel"] = relationship("Novel", back_populates="reviews")
    reviewer: Mapped["User"] = relationship("User", back_populates="reviews")
    
    __table_args__ = (
        CheckConstraint(
            "rating BETWEEN 1 AND 10",
            name="rating_between_1_and_10"
        ),
    )