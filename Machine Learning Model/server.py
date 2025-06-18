from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
ensemble_model = joblib.load("phishing_ensemble_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        url = data["url"]

        # Transform input URL
        features = vectorizer.transform([url])

        # Get prediction and confidence score
        proba = ensemble_model.predict_proba(features)[0]
        confidence = max(proba)

        # Apply confidence threshold rounding
        rounded_confidence = 1 if confidence > 0.96 else 0
        prediction = "phishing" if rounded_confidence == 1 else "safe"

        return jsonify({
            "url": url,
            "confidence": rounded_confidence,
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
