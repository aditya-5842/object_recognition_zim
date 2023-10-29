import os
import torch
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import supervision as sv


class SAM:
    def __init__(self, MODEL_TYPE="vit_b", MODEL_PATH="sam_vit_b_01ec64.pth"):
        self.DEVICE = torch.device("cpu")
        # self.DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.MODEL_TYPE = MODEL_TYPE
        self.CHECKPOINT_PATH = os.path.join(os.getcwd(), "data/weights", MODEL_PATH)
        self.sam = sam_model_registry[MODEL_TYPE](checkpoint=self.CHECKPOINT_PATH).to(device=self.DEVICE)
        self.mask_generator = SamAutomaticMaskGenerator(self.sam)

    def predict_bbox(self, image_rgb):
        sam_result = self.mask_generator.generate(image_rgb)
        detections = sv.Detections.from_sam(sam_result=sam_result)
        bboxes = detections.xyxy.tolist()
        return bboxes
