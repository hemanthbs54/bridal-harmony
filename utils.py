# utils.py
from PIL import Image

def validate_image(image: Image.Image) -> bool:
    """
    Basic check to see if image is valid for skin analysis.
    """
    return image.mode in ("RGB", "RGBA")
