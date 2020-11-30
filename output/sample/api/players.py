from typing import List, Optional
from fastapi import Header, APIRouter
from fastapi import HTTPException


from sample.dto.Player import PlayerIn, PlayerOut
from sample.api import db_manager

players = APIRouter()

@players.get('/players', response_model=List[PlayerOut], tags=["Players"])
async def index():
    return await db_manager.get_all_players()

@players.post('/player/', status_code=201, tags=["Players"])
async def add_player(payload: PlayerIn):
    player_id = await db_manager.add_player(payload)
    response = {
        'id': player_id,
        **payload.dict()
    }
    return response

@players.put('/player/{id}', tags=["Players"])
async def update_player(id: int, payload: PlayerIn, tags=["players"]):
    player = await db_manager.get_player(id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    update_data = payload.dict(exclude_unset=True)
    player_in_db = PlayerIn(**player)
    updated_player = player_in_db.copy(update=update_data)
    return await db_manager.update_player(id, updated_player)

@players.delete('/player/{id}', tags=["Players"])
async def delete_player(id: int):
    player = await db_manager.get_player(id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return await db_manager.delete_player(id)

    