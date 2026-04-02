from flask import Flask, render_template, request, jsonify, send_from_directory
import joblib
import numpy as np
import traceback
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load model with fallback
try:
    model = joblib.load('model.pkl')
    print("✅ Model loaded successfully!")
except:
    print("⚠️ No model.pkl found. Using demo model...")
    class DemoModel:
        def predict(self, X):
            amount = X[0, -1]
            return np.array([1 if amount > 1000 else 0])
        def predict_proba(self, X):
            amount = X[0, -1]
            prob = min(amount / 5000, 0.95)
            return np.array([[1-prob, prob]])
    model = DemoModel()

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    """Serve the predict page"""
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for predictions"""
    try:
        data = request.json
        print(f"📥 Received: {len(data)} features")
        
        # Exact 30 features in correct order
        feature_order = [
            'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
            'V10','V11','V12','V13','V14','V15','V16','V17','V18','V19',
            'V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'
        ]
        
        features = np.zeros((1, 30))
        for i, feature in enumerate(feature_order):
            features[0, i] = float(data.get(feature, 0))
        
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]
        
        print(f"🎯 Predicted: {'FRAUD' if prediction else 'LEGIT'}")
        
        return jsonify({
            'success': True,
            'prediction': 'FRAUD' if prediction == 1 else 'LEGITIMATE',
            'confidence': float(max(probs) * 100),
            'fraud_probability': float(probs[1] * 100)
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/about')
def about():
    return render_template('about.html')

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    print("🚀 Starting Fraud Detection Server...")
    print("📱 Visit: http://localhost:5000")
    print("🔍 Demo: http://localhost:5000/predict")
    app.run(debug=True, host='0.0.0.0', port=5000)