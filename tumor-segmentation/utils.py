
import numpy as np
import cv2
import base64 
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


def validate_segmentation(pet_mip, seg_pred):
    assert isinstance(
        seg_pred, np.ndarray), "Segmentation was not succesfully decoded as a numpy array"
    assert pet_mip.shape == seg_pred.shape, f"Segmentation of shape {seg_pred.shape} is not identical to image shape {pet_mip.shape}"

    unique_vals = list(np.unique(seg_pred))
    allowed_vals = [0, 255]
    unique_vals_str = ", ".join([str(x) for x in (unique_vals)])
    all_values_are_allowed = all(
        x in allowed_vals for x in unique_vals)
    assert all_values_are_allowed,  f"The segmentation contains values {{{unique_vals_str}}} but only values {{0,255}} are allowed"

    assert np.all(seg_pred[:, :, 0] == seg_pred[:, :, 1]) & np.all(
        seg_pred[:, :, 1] == seg_pred[:, :, 2]), "The segmentation values should be identical along the 3 color channels."

def dice_score(y_true: np.ndarray, y_pred:np.ndarray):
    y_true_bin = y_true > 0
    y_pred_bin = y_pred > 0
    return 2 * (y_true_bin & y_pred_bin).sum() / (y_true_bin.sum() + y_pred_bin.sum())

def encode_request(np_array: np.ndarray) -> str:
    # Encode the NumPy array as a png image
    success, encoded_img = cv2.imencode('.png', np_array)
    
    if not success:
        raise ValueError("Failed to encode the image")
    
    # Convert the encoded image to a base64 string
    base64_encoded_img = base64.b64encode(encoded_img.tobytes()).decode()
    
    return base64_encoded_img


def decode_request(request) -> np.ndarray:
    encoded_img: str = request.img
    np_img = np.fromstring(base64.b64decode(encoded_img), np.uint8)
    a = cv2.imdecode(np_img, cv2.IMREAD_ANYCOLOR)
    return a


def plot_prediction(mip,seg,seg_pred):

    score = dice_score(seg,seg_pred)
    print("Dice Score:", dice_score(seg,seg_pred))
    plt.figure(figsize=(9.2,3))

    plt.subplot(1,4,1)
    plt.imshow(mip)
    plt.axis("off")
    plt.title("PET MIP")

    plt.subplot(1,4,2)
    plt.imshow(seg)
    plt.axis("off")
    plt.title("True Segmentation")

    plt.subplot(1,4,3)
    plt.imshow(seg_pred)
    plt.axis("off")
    plt.title("Predicted Segmentation")

    TP = ((seg_pred>0)&(seg>0))[:,:,:1]
    FP = ((seg_pred>0)&(seg==0))[:,:,:1]
    FN = ((seg_pred==0)&(seg>0))[:,:,:1]
    img = np.concatenate((FP,TP,FN),axis=2).astype(np.uint8)*255

    plt.subplot(1,4,4)
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"dice score = {score:.02f}")
    plt.legend(["a","b"])

    # Create green, red, and blue squares as proxy artists
    green_square = mpatches.Patch(color='green', label='TP')
    red_square = mpatches.Patch(color='red', label='FP')
    blue_square = mpatches.Patch(color='blue', label='FN')

    # Add the proxy artists to the legend
    plt.legend(handles=[green_square, red_square, blue_square],loc="lower right")
    plt.tight_layout(h_pad=2,w_pad=0,pad=1.5)
    plt.show()
