from fastapi import FastAPI
import add_router
app = FastAPI()
app.include_router(add_router.router)



@app.get('/')
def home():
    return {
        "message": 'Here goes the beginning of the FastAPI journey'
    }


# @app.get('/numbers')
# def adding_numbers():
#     return f'message(s): Addition of numbers page'


# @app.get('/strings')
# def add_strings():
#     return {
#         'message': 'addition of strings page'
    # }

