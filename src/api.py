from flask import Flask, jsonify, request
from classifier import get_prediction

app = Flask(__name__)
@app.route('/predict-digit', methods=["POST"])

def predict_digit():
    image = request.files.get("digit")
    pred = get_prediction(image)
    return jsonify({
        "status":"success",
        "prediction":pred
    },200)
    
if __name__ == "__main__":
    app.run(debug=True)
    
