from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    """
    Schema for user registration.
    """

    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserResponse(BaseModel):
    """
    Safe user response (no password exposed).
    """

    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True
        
class UserLogin(BaseModel):
    """
    Schema for login.
    """
    
    username: str
    password: str
    
class TokenResponse(BaseModel):
    """
    JWT token response.
    """
    access_token: str
    token_type: str