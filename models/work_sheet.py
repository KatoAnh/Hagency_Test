from sqlalchemy import Column, Integer, Date, String, ForeignKey, UniqueConstraint
from connect.session import Base

class WorkSheet(Base):
    __tablename__ = "work_sheets"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    work_day = Column(Date, nullable=False)
    shift = Column(String, nullable=False) 

    __table_args__ = (
        UniqueConstraint("employee_id", "work_day", name="uq_employee_workday"),
    )

