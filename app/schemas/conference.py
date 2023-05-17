from typing import Optional
from datetime import datetime 
from pydantic import BaseModel 


class ConferenceBase(BaseModel):
    title: str 
    description: Optional[str] = None 
    start_time: datetime
    end_time: datetime
    Capacity: int 

# Shared properties
class ConferenceCreate(ConferenceBase):
    pass 

class ConferenceUpdate(ConferenceBase):
    title: Optional[str] = None
    description: Optional[str] = None 
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    Capacity: Optional[int] = None



class ConferenceIn(ConferenceBase):
    pass 

class ConferenceOut(ConferenceBase):
    pass
