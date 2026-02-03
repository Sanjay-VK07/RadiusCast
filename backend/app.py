from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from flask import Flask, jsonify, request, send_from_directory
import os
from utils.data_manager import prepare_features
from utils.geo_utils import within_5km

app = Flask(__name__)
CORS(app)

# Load region-specific models
models = {
    "Chennai": pickle.load(open("models/chennai.pkl", "rb")),
    "Madurai": pickle.load(open("models/madurai.pkl", "rb")),
    "Coimbatore": pickle.load(open("models/coimbatore.pkl", "rb"))
}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Validate region
    region = data.get("region")
    if region not in models:
        return jsonify({"error": "Invalid region selected"}), 400

    model = models[region]

    features = np.array([[
        data["temperature"],
        data["humidity"],
        data["windSpeed"],
        data["pressure"]
    ]])

    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0].max() * 100

    print("Region:", region, "| Prediction:", prediction)

    return jsonify({
        "willRain": int(prediction),
        "confidence": round(confidence, 2)
    })
    
    
@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")


if __name__ == "__main__":
    app.run(debug=True)

