from pydantic import BaseModel, EmailStr

# This defines what data we EXPECT from the user when they sign up
class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

# This defines what data we EXPECT from the user when they log in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# This defines what data we SEND BACK to the frontend (never send the password!)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True

# This is what we return when login is successful (includes the VIP token)
class Token(BaseModel):
    access_token: str
    token_type: str