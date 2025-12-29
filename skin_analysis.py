# skin_analysis.py
import cv2
import numpy as np
from PIL import Image

def analyze_skin(image: Image.Image) -> dict:
    """
    Analyze the uploaded PIL image and return skin metrics.
    """
    try:
        # Convert PIL to OpenCV
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        brightness = float(np.mean(cv_image))
        redness = int(np.mean(cv_image[:, :, 2]))  # R channel
        avg_color = cv2.mean(cv_image)[:3]
        skin_tone = {"R": int(avg_color[2]), "G": int(avg_color[1]), "B": int(avg_color[0])}

        return {
            "brightness": brightness,
            "skin_tone": skin_tone,
            "redness": redness
        }
    except Exception as e:
        return {"error": str(e)}
