from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_class import Base



class Conference(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    start_time = Column(DateTime, nullable= False)
    end_time = Column(DateTime, nullable= False)
    Capacity = Column(Integer, index=True, nullable= False)