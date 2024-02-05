# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get('/')
# def read_root():
#     return {'Hello': 'World'}


# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: Union[str, int] = None):
#     return {'item_id': item_id, 'q': q}


# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: Item):
#     return {'item_name': item.name, 'item_id': item_id}



from fastapi import FastAPI
import add_router as ar

app = FastAPI()
app.include_router(ar.router)


@app.get('/')
def home():
    return {
        "message": 'Here goes the beginning of the FastAPI journey'
    }


@app.get('/add/numbers')
def adding_numbers():
    return {
        "message": 'Addition of numbers page'
    }


@app.get('/add/strings')
def add_strings():
    return {
        'message': 'addition of strings page'
    }

