from enum import Enum
from pydantic import BaseModel
from datetime import date


class GenreURLChoices(Enum):    #TO SET ONLY POSSIBLE OPTIONS IN THE ROUTE
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


class Album(BaseModel):    #FOR ALBUMS LIST UNDER PYDANTIC SCHEMA
    title: str
    release_date: date


class BandBase(BaseModel):        #PYDANTIC SCHEMA FOR BANDS
    name: str
    genre: str
    albums: list[Album] = []  #Albums list along with default value

class BandCreate(BandBase):
    pass

class BandWithID(BandBase):
    id : int