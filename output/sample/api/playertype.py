from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ForeignKey, ARRAY)

from databases import Database
import sample.api.app_config

DATABASE_URL = sample.api.app_config.POSTGRES_CONNECTION

engine = create_engine(DATABASE_URL)
metadata = MetaData()
playertypes = Table(
    'playertype',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
    )

players = Table(
    'player',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('playertype', Integer, ForeignKey("playertype.id")),
    Column('genre', String(50), default="Test Genre"),
    Column('skills', ARRAY(String)),
    Column('interests', ARRAY(String))
    )
database = Database(DATABASE_URL)