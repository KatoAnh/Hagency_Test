from pydantic import BaseModel, validator
from datetime import date

class WorkScheduleUpdate(BaseModel):
    employee_id: int
    work_day: date
    shift: str

    @validator("shift")
    def validate_shift(cls, v):
        allowed = {"morning", "afternoon", "full_day"}
        if v not in allowed:
            raise ValueError("Ca Làm Việc phải là: morning, afternoon, hoặc full_day")
        return v
