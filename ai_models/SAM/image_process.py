import numpy as np

from ai_models.SAM.sam_model import SAM

SAM_MODEL = SAM()


def predict(img: np.ndarray):
    bbox = SAM_MODEL.predict_bbox(img)
    return bbox
