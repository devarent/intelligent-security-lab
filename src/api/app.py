"""
Flask API for Cyber Security ML Dashboard
Provides endpoints for predictions and model performance
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__, static_folder='../../dashboard', static_url_path='/dashboard')
CORS(app)

# Global variables for models
isolation_forest = None
ensemble_model = None

# Load models on startup
def load_models():
    global isolation_forest, ensemble_model
    try:
        if os.path.exists('data/models/isolation_forest.pkl'):
            isolation_forest = joblib.load('data/models/isolation_forest.pkl')
            print("Isolation Forest model loaded")
    except Exception as e:
        print(f"Isolation Forest model not found, running without it: {e}")

    try:
        if os.path.exists('data/models/ensemble_rf.pkl'):
            from src.models.ensemble_model import EnsembleModel
            ensemble_model = EnsembleModel()
            ensemble_model.load_models('data/models/ensemble')
            print("Ensemble model loaded")
    except Exception as e:
        print(f"Ensemble model not found, running without it: {e}")

# Load models at startup
load_models()

@app.route('/')
def index():
    """Serve the dashboard"""
    try:
        return send_from_directory('../../dashboard', 'index.html')
    except Exception as e:
        return jsonify({'message': 'Dashboard available at dashboard/index.html', 'error': str(e)})

@app.route('/dashboard')
def dashboard():
    """Serve the dashboard"""
    try:
        return send_from_directory('../../dashboard', 'index.html')
    except Exception as e:
        return jsonify({'message': 'Dashboard available at dashboard/index.html', 'error': str(e)})

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'isolation_forest_loaded': isolation_forest is not None,
        'ensemble_loaded': ensemble_model is not None
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Endpoint untuk prediksi"""
    data = request.json

    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    try:
        # Convert to numpy array
        features = np.array(data['features'])

        # Reshape if single sample
        if len(features.shape) == 1:
            features = features.reshape(1, -1)

        # Use ensemble model if available
        if ensemble_model:
            prediction = ensemble_model.predict(features)
            probability = ensemble_model.predict_proba(features)

            return jsonify({
                'model': 'ensemble',
                'prediction': prediction.tolist(),
                'probability': probability.tolist(),
                'status': 'success'
            })
        else:
            return jsonify({'error': 'No model loaded'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict/anomaly', methods=['POST'])
def predict_anomaly():
    """Endpoint untuk deteksi anomali menggunakan Isolation Forest"""
    data = request.json

    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    try:
        features = np.array(data['features'])

        if len(features.shape) == 1:
            features = features.reshape(1, -1)

        if isolation_forest:
            prediction = isolation_forest.predict(features)
            anomaly_score = isolation_forest.predict_anomaly_score(features)

            # Convert prediction: -1 (anomaly) -> 1, 1 (normal) -> 0
            prediction_binary = np.where(prediction == -1, 1, 0)

            return jsonify({
                'model': 'isolation_forest',
                'prediction': prediction_binary.tolist(),
                'anomaly_score': anomaly_score.tolist(),
                'status': 'success'
            })
        else:
            return jsonify({'error': 'Isolation Forest model not loaded'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/performance', methods=['GET'])
def get_performance():
    """Endpoint untuk mendapatkan metrik kinerja model"""
    # Performance metrics from the thesis (example values)
    performance = {
        'ensemble': {
            'accuracy': 0.9689,
            'precision': 0.9612,
            'recall': 0.9645,
            'f1_score': 0.9628,
            'roc_auc': 0.9876
        },
        'isolation_forest': {
            'accuracy': 0.8945,
            'precision': 0.8723,
            'recall': 0.9134,
            'f1_score': 0.8925
        },
        'cnn': {
            'accuracy': 0.9245,
            'precision': 0.9212,
            'recall': 0.9234,
            'f1_score': 0.9223
        },
        'gcn': {
            'accuracy': 0.8523,
            'precision': 0.8456,
            'recall': 0.8512,
            'f1_score': 0.8484
        }
    }
    return jsonify(performance)

@app.route('/api/threat-intel', methods=['POST'])
def threat_intelligence():
    """Endpoint untuk analisis intelijen ancaman"""
    data = request.json
    instruction = data.get('instruction', '')

    # Example threat intelligence response
    response = {
        'analysis': f"Based on the analysis of the provided data, potential threat patterns have been identified.",
        'recommendations': [
            "Implement rate limiting to mitigate DDoS attacks",
            "Enable advanced monitoring for unusual traffic patterns",
            "Review firewall rules and access controls",
            "Consider implementing SIEM for centralized monitoring"
        ],
        'confidence': 0.87,
        'status': 'success'
    }

    return jsonify(response)

@app.route('/api/history', methods=['GET'])
def get_history():
    """Endpoint untuk mendapatkan riwayat prediksi"""
    # Example historical data
    history = {
        'total_predictions': 15432,
        'threats_detected': 1245,
        'false_positives': 87,
        'trend': [
            {'date': '2024-01-01', 'threats': 45},
            {'date': '2024-01-02', 'threats': 52},
            {'date': '2024-01-03', 'threats': 38},
            {'date': '2024-01-04', 'threats': 67},
            {'date': '2024-01-05', 'threats': 55},
            {'date': '2024-01-06', 'threats': 71},
            {'date': '2024-01-07', 'threats': 49}
        ]
    }
    return jsonify(history)

if __name__ == '__main__':
    print("Starting Cyber Security ML Dashboard API...")
    print("Dashboard will be available at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
