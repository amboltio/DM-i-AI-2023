#%%
from matplotlib import pyplot as plt
from utils import dice_score, plot_prediction
from router import predict
import cv2

PATIENT_IX = "006"

img_f = f"data/patients/imgs/patient_{PATIENT_IX}.png"
seg_f = f"data/patients/labels/segmentation_{PATIENT_IX}.png"

img = cv2.imread(img_f)
seg = cv2.imread(seg_f)
seg_pred = predict(img)

plot_prediction(img,seg,seg_pred)

