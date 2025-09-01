from sqlalchemy.orm import Session
from models.work_sheet import WorkSheet
from models.employees import Employee
from fastapi import HTTPException

def update_or_create_schedule(db: Session, employee_id: int, work_day, shift: str):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy nhân viên với id = {employee_id}"
        )
    work_user = db.query(WorkSheet).filter(
        WorkSheet.employee_id == employee_id,
        WorkSheet.work_day == work_day
    ).first()
    if work_user:
        if work_user.shift == shift:
            return {"message": "Ca làm việc đã giống nhau, không có thay đổi", "schedule": work_user}
        work_user.shift = shift
        db.commit()
        db.refresh(work_user)
        return {"message": "Đã cập nhật lịch làm việc", "schedule": work_user}
    else:
        new_work = WorkSheet(
            employee_id=employee_id,
            work_day=work_day,
            shift=shift
        )
        db.add(new_work)
        db.commit()
        db.refresh(new_work)
        return {"message": "Đã thêm mới lịch làm việc", "schedule": new_work}