from fastapi import FastAPI, HTTPException            #IMPORT
from enum import Enum

app = FastAPI() #INSTANCE OF FASTAPI

@app.get('/') #ROUTE
async def index() -> dict[str, str]: #ASYNC FUNCTION WITH PROPER RETURN TYPE
    return {'hello': 'world'}

@app.get('/about')
async def about() -> str:
    return 'AN EXCEPTIONAL COMPANY'


class GenreURLChoices(Enum):    #TO SET ONLY POSSIBLE OPTIONS IN THE ROUTE
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


#Demo data in format --> list[dict{str, str}]
BANDS = [       
     {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
     {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic' },
     {'id': 3, 'name': 'Black Sabbath', 'genre': 'Metal'},
     {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands/{band_id}') #ROUTE
async def band(band_id: int) -> dict: #ASYNC WITH RETURN TYPE
  band = next((b for b in BANDS if b['id'] == band_id), None)
  if band is None: 
    raise HTTPException(status_code = 404, detail = 'Band not found')
  return band


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return[
      b for b in BANDS if b['genre'].lower() == genre.value
    ]
