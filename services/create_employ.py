from sqlalchemy.orm import Session
from models.employees import Employee
from schemas.employee import EmployeeCreate


def create_employee(db: Session, emp: EmployeeCreate):
    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp
