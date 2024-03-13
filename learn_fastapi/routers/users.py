from fastapi import APIRouter, Path
from typing import Optional
from pydantic import BaseModel

router = APIRouter()


# GOALKEEPERS
# 1Aaron Ramsdale # 22David Raya  #31Karl Hein
# DEFENDERS
# 2William Saliba  # 4Ben White  # 6Gabriel # 12Jurrien Timber # 15Jakub Kiwior # 17Cedric Soares
# 18Takehiro Tomiyasu # 35Oleksandr Zinchenko
# MIDFIELDERS
# 5Thomas Partey # 8Martin Odegaard # 10Emile Smith Rowe # 20Jorginho # 21Fabio Vieira # 25Mohamed Elneny 
# 29Kai Havertz # 41Declan Rice
# FORWARDS
# 7Bukayo Saka # 9Gabriel Jesus # 11Gabriel Martinelli # 14Eddie Nketiah # 19Leandro Trossard # 24Reiss Nelson


Arsenal = {
    22: {
        'name': 'raya',
        'pos': 'gk',
        'shirt number': '22',
    },
    1: {
        'name': 'ramsdale',
        'pos': 'gk',
        'shirt number': '1',
    },
    31: {
        'name': 'hein',
        'pos': 'gk',
        'shirt number': '31'
    },
    2: {
        'name': 'saliba',
        'pos': 'def',
        'shirt number': 2
    },
    4: {
        'name': 'white',
        'pos': 'def',
        'shirt number': '4'
    },
    6: {
        'name': 'gabriel',
        'pos': 'def',
        'shirt number': '6'
    },
}

Ars = {
    'rams': {
        'name': 'ramsdale',
        'pos': 'gk',
        'shirt number': '1',
    },
}

class Players(BaseModel):
    name: str
    pos: str
    shirt_number: int


@router.post('create-player/{player_id}')
def create_player(player_id : int, ars : Players):
    if player_id in Arsenal:
        return {'Error': 'Player already exits'}
    
    Arsenal[player_id] = ars
    return Arsenal[player_id]
    



@router.get("/players/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/players/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/players/sh/{shirt_number}", tags=["users"])
async def read_user(shirt_number: int):
    return {shirt_number: Arsenal[shirt_number]}


@router.get('/get')
async def get_user(*, name: Optional[str] = None, shirt_number : int):
    for players in Arsenal:
        if Arsenal[players]['name'] or Arsenal[players]['shirt number'] == name or shirt_number:
            return Arsenal[players]
    return 'Player not found'

