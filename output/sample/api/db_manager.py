from sample.dto.PlayerType import PlayertypeIn, PlayertypeOut, PlayertypeUpdate
from sample.api.db import playertypes
from sample.dto.Player import PlayerIn, PlayerOut, PlayerUpdate
from sample.api.db import players

from sample.api.db import database
async def add_playertype(payload: PlayertypeIn):
    query = playertypes.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_playertypes():
    query = playertypes.select()
    return await database.fetch_all(query=query)

async def get_playertype(id):
    query = playertypes.select(playertypes.c.id==id)
    return await database.fetch_one(query=query)

async def delete_playertype(id: int):
    query = playertypes.delete().where(playertypes.c.id==id)
    return await database.execute(query=query)

async def update_playertype(id: int, payload: PlayertypeIn):
    query = (
        playertypes
        .update()
        .where(playertypes.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
async def add_player(payload: PlayerIn):
    query = players.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_players():
    query = players.select()
    return await database.fetch_all(query=query)

async def get_player(id):
    query = players.select(players.c.id==id)
    return await database.fetch_one(query=query)

async def delete_player(id: int):
    query = players.delete().where(players.c.id==id)
    return await database.execute(query=query)

async def update_player(id: int, payload: PlayerIn):
    query = (
        players
        .update()
        .where(players.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
