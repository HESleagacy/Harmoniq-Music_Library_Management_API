from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date


class GenreURLChoices(Enum):    #TO SET ONLY POSSIBLE OPTIONS IN THE ROUTE
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'

class GenreChoices(Enum):    #TO SET ONLY POSSIBLE OPTIONS IN THE ROUTE
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-hop'


class Album(BaseModel):    #FOR ALBUMS LIST UNDER PYDANTIC SCHEMA
    title: str
    release_date: date


class BandBase(BaseModel):        #PYDANTIC SCHEMA FOR BANDS
    name: str
    genre: GenreChoices
    albums: list[Album] = []  #Albums list along with default value

class BandCreate(BandBase):
    @field_validator('genre', mode = 'before')
    def title_case_genre(cls, value):
        return value.title() #converts the string to title case


class BandWithID(BandBase):
    id : int