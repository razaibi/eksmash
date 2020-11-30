from typing import List, Optional
from pydantic import BaseModel


class PlayertypeIn(BaseModel):
    name : str
    
    
    class Config:
        arbitrary_types_allowed = True

class PlayertypeOut(PlayertypeIn):
    id : int
    
    class Config:
        arbitrary_types_allowed = True

class PlayertypeUpdate(BaseModel):
    name : None
    

    class Config:
        arbitrary_types_allowed = True