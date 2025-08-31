from sqlalchemy.orm import Session
from models.employees import Employee
from typing import Optional 

def list_employees(
        db: Session, department: Optional[str] = None,
        skip : int = 0,
        limit : int = 10
        )-> list[Employee]:
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department == department)
    return query.offset(skip).limit(limit).all()
