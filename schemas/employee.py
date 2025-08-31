from pydantic import BaseModel , EmailStr
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    position: str | None = None
    department: str | None = None
    start_date: date | None = None

class EmployeeOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    position: str | None = None
    department: str | None = None
    start_date: date | None = None

    class Config:
        orm_mode = True