import json
import os
from typing import List
import uvicorn
import cv2
from fastapi import Body, FastAPI, HTTPException, status, UploadFile

import numpy as np


from ai_models.SAM import predict
from ai_models.utils import InvalidFileExtension, allowed_file

app = FastAPI()


@app.get("/health")
async def read_root():
    return {"status": "running"}


@app.post("/get_bbox_detections")
async def get_bbox(files: UploadFile):
    try:
        if allowed_file(files.filename):
            # write the file
            with open(files.filename, "wb") as f:
                f.write(await files.read())

            # read the file
            img = cv2.imread(filename=files.filename)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            print(img_rgb.shape)
            #  predict
            bbox = predict(img_rgb)
            os.remove(files.filename)
            # remove the file
            return {"status": "Success", "filename": files.filename, "bboxes": bbox}
        else:
            raise InvalidFileExtension
    except InvalidFileExtension as e:
        return {"status": "Failed", "message": f"Wrong file extension: {e}"}
    except Exception as e:
        return {"status": "Failed", "message": f"{e}"}


if __name__ == "__main__":
    uvicorn.run(app)
