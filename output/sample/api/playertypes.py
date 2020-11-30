from typing import List, Optional
from fastapi import Header, APIRouter
from fastapi import HTTPException


from sample.dto.PlayerType import PlayertypeIn, PlayertypeOut
from sample.api import db_manager

playertypes = APIRouter()

@playertypes.get('/playertypes', response_model=List[PlayertypeOut], tags=["PlayerTypes"])
async def index():
    return await db_manager.get_all_playertypes()

@playertypes.post('/playertype/', status_code=201, tags=["PlayerTypes"])
async def add_playertype(payload: PlayertypeIn):
    playertype_id = await db_manager.add_playertype(payload)
    response = {
        'id': playertype_id,
        **payload.dict()
    }
    return response

@playertypes.put('/playertype/{id}', tags=["PlayerTypes"])
async def update_playertype(id: int, payload: PlayertypeIn, tags=["playertypes"]):
    playertype = await db_manager.get_playertype(id)
    if not playertype:
        raise HTTPException(status_code=404, detail="Playertype not found")
    update_data = payload.dict(exclude_unset=True)
    playertype_in_db = PlayertypeIn(**playertype)
    updated_playertype = playertype_in_db.copy(update=update_data)
    return await db_manager.update_playertype(id, updated_playertype)

@playertypes.delete('/playertype/{id}', tags=["PlayerTypes"])
async def delete_playertype(id: int):
    playertype = await db_manager.get_playertype(id)
    if not playertype:
        raise HTTPException(status_code=404, detail="Playertype not found")
    return await db_manager.delete_playertype(id)

    