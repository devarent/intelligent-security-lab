"""
Script untuk menjalankan Flask API Server dari root directory
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("=" * 80)
print("CYBER SECURITY ML DASHBOARD - FLASK API SERVER")
print("=" * 80)
print()

# Check if data directory exists
if not os.path.exists('data/models'):
    print("Membuat direktori data/models...")
    os.makedirs('data/models', exist_ok=True)

print("Starting Flask API Server...")
print("Dashboard akan tersedia di: http://localhost:5000")
print("API endpoints:")
print("  - http://localhost:5000/ (Dashboard)")
print("  - http://localhost:5000/api/health (Health Check)")
print("  - http://localhost:5000/api/predict (Prediction)")
print("  - http://localhost:5000/api/performance (Performance Metrics)")
print()
print("Tekan Ctrl+C untuk menghentikan server")
print("=" * 80)
print()

# Import and run Flask app
from api.app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
