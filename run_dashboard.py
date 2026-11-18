"""
Script untuk menjalankan Dashboard Cyber Security ML
"""

import os
import sys
import subprocess

print("=" * 80)
print("CYBER SECURITY ML DASHBOARD")
print("=" * 80)
print()

# Check if data directory exists
if not os.path.exists('data/models'):
    print("Membuat direktori data/models...")
    os.makedirs('data/models', exist_ok=True)

print("Starting Flask API Server...")
print("Dashboard akan tersedia di: http://localhost:5000")
print("Atau buka file: dashboard/index.html langsung di browser (mode offline)")
print()
print("Tekan Ctrl+C untuk menghentikan server")
print("=" * 80)
print()

# Run Flask app using start_server.py
try:
    subprocess.run([sys.executable, 'start_server.py'])
except KeyboardInterrupt:
    print("\n\nServer dihentikan.")
except Exception as e:
    print(f"\n\nError starting server: {e}")
