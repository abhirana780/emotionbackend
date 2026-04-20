from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Load model, vectorizer, encoder
# Files are in the same directory as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "emotion_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))
le = pickle.load(open(os.path.join(BASE_DIR, "label_encoder.pkl"), "rb"))

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'user_text' not in data:
        return jsonify({"error": "Missing user_text"}), 400
    
    user_text = data['user_text']
    text_vector = vectorizer.transform([user_text])
    prediction = model.predict(text_vector)[0]
    emotion = le.inverse_transform([prediction])[0]
    
    return jsonify({
        "user_text": user_text,
        "emotion": emotion.title()
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

