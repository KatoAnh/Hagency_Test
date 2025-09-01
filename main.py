from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from connect.session import Base, engine, get_db  
from services import create_employ
from schemas.employee import EmployeeCreate, EmployeeOut
from typing import List, Optional 
import services.list_employ as sevice
from datetime import datetime
from schemas.work_sheet import WorkScheduleUpdate
from services.work_sheet import update_or_create_schedule


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/add_employee/", response_model=EmployeeOut)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employ.create_employee(db, emp)

@app.get("/employees", response_model=List[EmployeeOut])
def get_employees(
                department : Optional[str] = None,
                start_date_after: Optional[str] = None, 
                page: int = Query(1, ge=1),
                limit: int = Query(10, ge=1, le=20),
                db: Session = Depends(get_db)
                  ):
    skip = (page - 1) * limit
    # Chỉ gọi service, không xử lý logic ở đây
    return sevice.list_employees(
        db,
        department=department,
        start_date_after=start_date_after,
        skip=skip,
        limit=limit
    )

@app.post("/work-schedule/update")
def update_work_schedule(
    data: WorkScheduleUpdate,
    db: Session = Depends(get_db)
):
    # Chỉ gọi service, không xử lý logic ở đây
    return update_or_create_schedule(
        db,
        employee_id=data.employee_id,
        work_day=data.work_day,
        shift=data.shift
    )