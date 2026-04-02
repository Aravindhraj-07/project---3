from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([[
            data['Time'], data['V1'], data['V2'], data['V3'], data['V4'],
            data['V5'], data['V6'], data['V7'], data['V8'], data['V9'],
            data['V10'], data['V11'], data['V12'], data['V13'], data['V14'],
            data['V15'], data['V16'], data['V17'], data['V18'], data['V19'],
            data['V20'], data['V21'], data['V22'], data['V23'], data['V24'],
            data['V25'], data['V26'], data['V27'], data['V28'], data['Amount']
        ]])
        
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        
        return jsonify({
            'prediction': 'FRAUD' if prediction == 1 else 'LEGITIMATE',
            'confidence': max(probability) * 100,
            'fraud_probability': probability[1] * 100 if len(probability) > 1 else 0
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)