import json
import os

import uvicorn
from fastapi import Body, FastAPI, HTTPException, status


# load the ml model
# model = YOLO(settings.ml_model_path)


app = FastAPI()



@app.get("/")
async def read_root():
    return "Started"




if __name__ == "__main__":
    uvicorn.run(app)
