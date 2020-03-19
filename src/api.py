from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def hello():
    return jsonify({"class": "This item has been identified to belong to cool class"})

if __name__ == '__main__':
    app.run(debug=True)
