import tensorflow as tf
import numpy as np
from utils import transform_image
import io
from PIL import Image

def get_predictions(model, image):

    image = Image.open(io.BytesIO(image))
    image = transform_image(image)
    y_pred = model.predict(image)
    return np.argmax(y_pred)
