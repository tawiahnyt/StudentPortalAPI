from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentData(Base):
    __tablename__ = "student_data"
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    other_name = Column(String, nullable=True)
    date_of_birth = Column(Date)
    phone = Column(String)
    email = Column(String)
    student_email = Column(String)
    gender = Column(String)
    level = Column(String)
    student_type = Column(String)
    enrollment_date = Column(String)
    graduation_date = Column(String)
    degree_programmes = Column(String)
    guardian_name = Column(String)
    guardian_email = Column(String, nullable=True)
    guardian_phone = Column(String)
    guardian_address = Column(String)
    password = Column(String)
    registration_status = Column(Integer)