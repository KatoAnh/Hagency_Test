from sqlalchemy import Column, Integer, String ,Date
from connect.session import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True,nullable=False)
    position = Column(String, nullable=True)
    department = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
