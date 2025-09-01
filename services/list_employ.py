from sqlalchemy.orm import Session
from models.employees import Employee
from typing import Optional
from datetime import datetime
from fastapi import HTTPException

def list_employees(
    db: Session,
    department: Optional[str] = None,
    start_date_after: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
) -> list[Employee]:
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department.ilike(department.strip()))
    if start_date_after:
        try:
            date = datetime.strptime(start_date_after, "%Y-%m-%d").date()
        except Exception:
            raise HTTPException(
                status_code=422,
                detail=" Ngày Tháng Năm phải nhập theo định dạng YYYY-MM-DD (ví dụ: 2025-09-01)"
            )
        query = query.filter(
            Employee.start_date.isnot(None),
            Employee.start_date > date
        )
    return query.offset(skip).limit(limit).all()

