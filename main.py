from fastapi import FastAPI, Depends,Query
from sqlalchemy.orm import Session
from connect.session import Base, engine, get_db  
from services import create_employ
from schemas.employee import EmployeeCreate, EmployeeOut
from typing import List, Optional 
import services.list_employ as sevice


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
                page: int = Query(1, ge=1),
                limit: int = Query(10, ge=1, le=20),
                db: Session = Depends(get_db)
                  ):
    skip = (page - 1) * limit
    return sevice.list_employees(db, department,skip=skip,limit=limit)