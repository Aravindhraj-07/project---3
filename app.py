import traceback

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("Received data keys:", list(data.keys()))  # Debug
        
        # Validate all 30 features
        required_features = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
                           'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
                           'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
        
        features = np.zeros((1, 30))
        for i, feature in enumerate(required_features):
            features[0, i] = float(data.get(feature, 0.0))
        
        print("Feature shape:", features.shape)  # Debug
        
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        
        print(f"Prediction: {prediction}, Probs: {probability}")  # Debug
        
        return jsonify({
            'prediction': 'FRAUD' if prediction == 1 else 'LEGITIMATE',
            'confidence': float(max(probability) * 100),
            'fraud_probability': float(probability[1] * 100)
        })
    except Exception as e:
        print(f"PREDICTION ERROR: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 400