import numpy as np

def transform_image(image):
    image = np.array(image)
    image = image/255.0
    return np.expand_dims(image, axis=0)