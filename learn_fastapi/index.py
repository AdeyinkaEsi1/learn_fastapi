import imp
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    a = "aletra"
    resnet = "resnet"
    lenet = "lenet"
    l19 = 'leo'


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.a:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name is ModelName.l19:
        return {'player': model_name}
    pass
