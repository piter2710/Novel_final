from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
class UserCreate(UserBase):
    password: str

class UserPublic(BaseModel):
    user_id: int
    username: str
    
    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
class UserOut(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True, extra="ignore")
class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    
class UserPasswordUpdate(BaseModel):
    password: str
    new_password: str

class UserProfile(BaseModel):
    username: str
    
    created_at: datetime
    updated_at: datetime
    mdoel_config = ConfigDict(
        from_attributes=True, extra="ignore")