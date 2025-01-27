from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentResultsData(Base):
    __tablename__ = "results_data"
    student_id = Column(Integer, primary_key=True)
    level = Column(Integer)
    MATH_173 = Column(Integer)
    MATH_171 = Column(Integer)
    FREN_171 = Column(Integer)
    IT_133 = Column(Integer)
    METS_173 = Column(Integer)
    IT_101 = Column(Integer)
    SCOT_175 = Column(Integer)
    FREN_172 = Column(Integer)
    IT_102 = Column(Integer)
    IT_124 = Column(Integer)
    IT_152 = Column(Integer)
    MATH_176 = Column(Integer)
    ENG_174 = Column(Integer)
    AFRS_271 = Column(Integer)
    IT_231 = Column(Integer)
    IT_241 = Column(Integer)
    IT_245 = Column(Integer)
    FREN_273 = Column(Integer)
    IT_221 = Column(Integer)
    ENGL_275 = Column(Integer)
    IT_206 = Column(Integer)
    IT_274 = Column(Integer)
    IT_242 = Column(Integer)
    IT_222 = Column(Integer)
    IT_232 = Column(Integer)
    IT_204 = Column(Integer)
    IT_276 = Column(Integer)
    IT_323 = Column(Integer)
    IT_343 = Column(Integer)
    IT_313 = Column(Integer)
    IT_371 = Column(Integer)
    IT_391 = Column(Integer)
    IT_305 = Column(Integer)
    IT_301 = Column(Integer)
    IT_308 = Column(Integer)
    IT_302 = Column(Integer)
    IT_324 = Column(Integer)
    IT_344 = Column(Integer)
    IT_306 = Column(Integer)
