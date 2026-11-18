# Cyber Security ML - Machine Learning untuk Deteksi Ancaman Keamanan Siber

Proyek ini mengimplementasikan berbagai algoritma machine learning untuk deteksi ancaman keamanan siber, mencakup deteksi intrusi jaringan, klasifikasi malware, dan keamanan perangkat IoT.

## 📋 Daftar Isi

- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [VS Code dan ekstensi](#vs-code-dan-ekstensi)
- [Struktur Proyek](#struktur-proyek)
- [Penggunaan](#penggunaan)
- [Model yang Diimplementasikan](#model-yang-diimplementasikan)
- [Dataset](#dataset)
- [Dashboard](#dashboard)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## ✨ Fitur

- **Preprocessing Data**: Data cleaning, normalisasi, feature engineering, dan handling class imbalance
- **Deteksi Anomali**: Isolation Forest untuk real-time anomaly detection
- **Klasifikasi**: Ensemble model (Random Forest + XGBoost + LightGBM) untuk high-accuracy detection
- **Dashboard Web**: Monitoring real-time dan visualisasi kinerja model
- **Modular**: Kode yang terstruktur dengan baik dan mudah dikembangkan

## 🚀 Instalasi

### Prasyarat

- Python 3.9 atau 3.10
- pip atau conda
- (Opsional) GPU NVIDIA untuk training deep learning yang lebih cepat

### Langkah Instalasi

1. Clone repository:
```bash
git clone <repository-url>
cd "Keamanan Berbasis Sistem Cerdas"
```

2. Buat virtual environment (disarankan):
```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## VS Code dan ekstensi

Workspace ini merekomendasikan ekstensi inti untuk Python, Pylance, Jupyter, dan Ruff. Buka folder proyek di VS Code, lalu tinjau rekomendasi pada Extensions. Daftarnya ada di `.vscode/extensions.json`; rekomendasi tidak memasang ekstensi secara otomatis dan bukan daftar wajib untuk setiap proyek.

Untuk mengembangkan banyak jenis proyek, gunakan profil VS Code terpisah (Command Palette → `Profiles: Create Profile`), misalnya Python/ML, Web, DevOps/Containers, dan Quantum/Haskell. Ini mempertahankan ekstensi yang sudah terpasang tanpa mengaktifkan semua toolchain di setiap workspace. Ekstensi Python/Jupyter tidak memasang TensorFlow/Keras; pilih environment Python dan kernel proyek. Ekstensi Docker memerlukan Docker Engine/Desktop, dan Haskell maupun Q# memerlukan toolchain masing-masing. Pasang atau aktifkan toolchain sesuai profil proyek agar konflik dan beban pemindaian berkurang.

## 📁 Struktur Proyek

```
Keamanan Berbasis Sistem Cerdas/
├── data/
│   ├── raw/              # Dataset mentah
│   ├── processed/        # Dataset yang sudah dipreprocessing
│   └── models/           # Model yang sudah dilatih
├── src/
│   ├── preprocessing/    # Modul preprocessing
│   │   ├── data_cleaner.py
│   │   ├── feature_engineering.py
│   │   ├── imbalance_handler.py
│   │   └── data_splitter.py
│   ├── models/           # Implementasi model
│   │   ├── isolation_forest_model.py
│   │   ├── ensemble_model.py
│   │   ├── cnn_model.py
│   │   ├── gcn_model.py
│   │   └── llm_model.py
│   └── utils/            # Utility functions
├── dashboard/            # Frontend dashboard
├── docs/                 # Dokumentasi skripsi
│   ├── SKRIPSI.md
│   ├── BAB1_PENDAHULUAN.md
│   ├── BAB2_TINJAUAN_PUSTAKA.md
│   ├── BAB3_METODOLOGI_PENELITIAN.md
│   ├── BAB4_IMPLEMENTASI.md
│   ├── BAB5_HASIL_DAN_PEMBAHASAN.md
│   ├── BAB6_KESIMPULAN_DAN_SARAN.md
│   └── DAFTAR_PUSTAKA.md
├── main_training.py     # Script training utama
├── requirements.txt      # Dependencies
└── README.md            # Dokumentasi proyek
```

## 💻 Penggunaan

### Training Model

Jalankan script training utama:

```bash
python main_training.py
```

Script ini akan:
1. Load dan clean data
2. Feature engineering dan normalisasi
3. Handle class imbalance dengan SMOTE
4. Split data menjadi train/val/test
5. Train Isolation Forest model
6. Train Ensemble model
7. Evaluasi semua model
8. Simpan model yang sudah dilatih

### Preprocessing Data

```python
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.feature_engineering import FeatureEngineer
from src.preprocessing.imbalance_handler import ImbalanceHandler
from src.preprocessing.data_splitter import DataSplitter

# Load data
df = pd.read_csv('data/raw/dataset.csv')

# Clean data
cleaner = DataCleaner()
df_cleaned = cleaner.clean_data(df)

# Feature engineering
engineer = FeatureEngineer()
X = engineer.normalize_features(df_cleaned.drop('label', axis=1))

# Handle imbalance
handler = ImbalanceHandler()
X_resampled, y_resampled = handler.apply_smote(X, df_cleaned['label'])

# Split data
splitter = DataSplitter()
X_train, X_val, X_test, y_train, y_val, y_test = splitter.split_data(
    X_resampled, y_resampled
)
```

### Training Individual Models

#### Isolation Forest

```python
from src.models.isolation_forest_model import IsolationForestModel

iso_forest = IsolationForestModel(n_estimators=100, contamination=0.05)
iso_forest.train(X_train[y_train == 0])
iso_forest.evaluate(X_test, y_test)
iso_forest.save_model('data/models/isolation_forest.pkl')
```

#### Ensemble Model

```python
from src.models.ensemble_model import EnsembleModel

ensemble = EnsembleModel()
ensemble.build_base_models()
ensemble.train_base_models(X_train, y_train)
ensemble.train_meta_model(X_train, y_train, X_val, y_val)
ensemble.evaluate(X_test, y_test)
ensemble.save_models('data/models/ensemble')
```

### Inference (Prediksi)

```python
from src.models.ensemble_model import EnsembleModel

# Load model
ensemble = EnsembleModel()
ensemble.load_models('data/models/ensemble')

# Prediksi
predictions = ensemble.predict(new_data)
probabilities = ensemble.predict_proba(new_data)
```

## 🤖 Model yang Diimplementasikan

### 1. Isolation Forest
- **Tipe**: Unsupervised Learning
- **Use Case**: Real-time anomaly detection
- **Akurasi**: 89-91%
- **Kecepatan**: Sangat cepat (training: 45-248s, inference: 0.002s/sample)

### 2. Convolutional Neural Networks (CNN)
- **Tipe**: Deep Learning
- **Use Case**: Klasifikasi malware berbasis citra
- **Akurasi**: 92.45%
- **Dataset**: MalNet-Image

### 3. Graph Convolutional Networks (GCN)
- **Tipe**: Deep Learning on Graphs
- **Use Case**: Analisis relasional malware
- **Akurasi**: 85.23%
- **Use Case**: Forensik dan analisis relasi entitas

### 4. Ensemble Model (Stacking)
- **Tipe**: Supervised Learning (Ensemble)
- **Komponen**: Random Forest + XGBoost + LightGBM + Logistic Regression
- **Akurasi**: 96-97%
- **Kecepatan**: Cepat (inference: 0.025s/sample)

### 5. Large Language Models (LLM)
- **Tipe**: Generative AI
- **Use Case**: Threat intelligence dan analisis interpretatif
- **Dataset**: CyberLLMInstruct
- **BLEU Score**: 0.7234

## 📊 Dataset

Dataset yang digunakan dalam penelitian ini:

1. **CIC-IDS2017**: Intrusion detection dataset dengan 78 fitur
2. **CIC-IDS2018**: Intrusion detection dataset dengan 80 fitur
3. **CIC-DDoS2019**: DDoS attack dataset
4. **CIC-BCCC-NRC TabularIoTAttack-2024**: IoT security dataset
5. **MalNet-Image**: Malware image dataset untuk klasifikasi berbasis citra
6. **CyberLLMInstruct**: Instruction-response dataset untuk LLM fine-tuning

### Cara Download Dataset

Dataset dapat diunduh dari sumber resmi:

- CIC Datasets: https://www.unb.ca/cic/datasets/
- MalNet: https://malnet.org/
- CyberLLMInstruct: https://github.com/cyberllm-instruct

Letakkan dataset yang sudah diunduh di folder `data/raw/`.

## 🖥️ Dashboard

Dashboard web untuk monitoring real-time dan visualisasi dapat dijalankan dengan:

### Cara 1: Menggunakan start_server.py (Disarankan)

```bash
python start_server.py
```

### Cara 2: Menggunakan run_dashboard.py

```bash
python run_dashboard.py
```

Dashboard akan tersedia di http://localhost:5000

Alternatif: Anda juga dapat membuka file `dashboard/index.html` langsung di browser untuk mode offline (tanpa koneksi ke API server).

### Fitur Dashboard

- Real-time monitoring traffic jaringan
- Visualisasi kinerja model
- Confusion matrix interactive
- ROC curves
- Feature importance plots
- Threat intelligence analysis
- Export hasil ke CSV/PDF

## 📚 Dokumentasi Skripsi

Dokumentasi lengkap skripsi tersedia di folder `docs/`:

- `SKRIPSI.md`: Ringkasan skripsi lengkap
- `BAB1_PENDAHULUAN.md`: Latar belakang dan rumusan masalah
- `BAB2_TINJAUAN_PUSTAKA.md`: Review literatur dan teori
- `BAB3_METODOLOGI_PENELITIAN.md`: Metodologi dan framework
- `BAB4_IMPLEMENTASI.md`: Implementasi dan kode program
- `BAB5_HASIL_DAN_PEMBAHASAN.md`: Hasil dan analisis
- `BAB6_KESIMPULAN_DAN_SARAN.md`: Kesimpulan dan rekomendasi
- `DAFTAR_PUSTAKA.md`: Referensi dan sumber

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 Lisensi

Proyek ini adalah bagian dari skripsi dan untuk keperluan akademis. Hubungi penulis untuk penggunaan komersial atau redistribusi.

## 👤 Penulis

**Muhammad Arya Fatthurahman**
NIM: 2023230006
Program Studi Teknik Informatika
Fakultas Teknik
Universitas [Nama Universitas]

## 🙏 Acknowledgments

- Canadian Institute for Cybersecurity (CIC) untuk dataset yang komprehensif
- Kontributor open-source community untuk library machine learning
- Dosen pembimbing dan reviewer

## 📧 Kontak

Untuk pertanyaan atau diskusi, silakan hubungi penulis melalui email: [email]

---

**Catatan**: Proyek ini dikembangkan untuk penelitian skripsi dan tujuan akademis. Gunakan dengan bijak dan sesuai dengan regulasi yang berlaku.

---

## Project Governance

[![CI](https://github.com/aryafatthurahman4-collab/keamanan-berbasis-sistem-cerdas/actions/workflows/ci.yml/badge.svg)](https://github.com/aryafatthurahman4-collab/keamanan-berbasis-sistem-cerdas/actions/workflows/ci.yml)

[Contributing](CONTRIBUTING.md) | [Security Policy](SECURITY.md) | [Code of Conduct](CODE_OF_CONDUCT.md)