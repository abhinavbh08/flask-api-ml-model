import tensorflow as tf
from flask import Flask, jsonify, request
from predict import get_predictions
import json

app = Flask(__name__)
loaded_model = tf.keras.models.load_model("models/my_mnist_model.h5")

@app.route("/predict", methods=["POST"])
def predict():

    if request.method=="POST":
        file = request.files["file"]
        img_bytes = file.read()
        class_id = get_predictions(loaded_model, img_bytes)
        return jsonify({"class": "This item has been identified to belong to " + str(class_id)})

if __name__ == '__main__':
    app.run(debug=True)