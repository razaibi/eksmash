from typing import List, Optional
from pydantic import BaseModel


class PlayerIn(BaseModel):
    name : str
    playertype : int
    genre : str
    skills : List[str]
    interests : List[str]
    
    
    class Config:
        arbitrary_types_allowed = True

class PlayerOut(PlayerIn):
    id : int
    
    class Config:
        arbitrary_types_allowed = True

class PlayerUpdate(BaseModel):
    name : None
    playertype : None
    genre : None
    skills : None
    interests : None
    

    class Config:
        arbitrary_types_allowed = True