from fastapi import FastAPI
from sample.api.playertypes import playertypes

from sample.api.players import players

from sample.api.db import metadata, database, engine

tags_metadata = [
    {
        "name": "PlayerTypes",
        "description": "Interact with player types from here.",
    },

    {
        "name": "Players",
        "description": "Interact with players from here.",
    },

]

metadata.create_all(engine)
app = FastAPI(
    title="Sample",
    description="A test Web API for PyCon Sweden 2020",
    version="0.0.1",
    openapi_tags=tags_metadata
)



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
app.include_router(playertypes)

app.include_router(players)
