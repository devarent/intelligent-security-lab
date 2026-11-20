
<!-- identity-block -->
<div align="center">

# intelligent-security-lab

<sub>Riset dan prototipe keamanan berbasis sistem cerdas.</sub>

</div>

## At a glance

| Field | Detail |
| --- | --- |
| Repository | intelligent-security-lab |
| Primary language | Python |
| Topics | artificial-intelligence, cybersecurity, machine-learning, python, research, security |
| License | MIT |
| Branch | main |
| Maintainer | [@devarent](https://github.com/devarent) |

## Overview

intelligent-security-lab is a hands-on repository focused on: Riset dan prototipe keamanan berbasis sistem cerdas.. Primary language: Python. Topics: artificial-intelligence, cybersecurity, machine-learning, python, research, security. The README below documents the project; use the table above for a quick overview.

### Global references

<div align="center">

🇮🇸 Iceland &middot; 🇳🇿 New Zealand &middot; 🇨🇭 Switzerland &middot; 🇸🇮 Slovenia &middot; 🇮🇪 Ireland &middot; 🇦🇹 Austria &middot; 🇵🇹 Portugal &middot; 🇸🇬 Singapore &middot; 🇫🇮 Finland

</div>

---

<!-- dbx-style-kit -->
<div align="center">

<img src="https://img.shields.io/badge/keamanan-berbasis-sistem-cerdas-1f6feb?style=for-the-badge" alt="keamanan-berbasis-sistem-cerdas" />
<img src="https://img.shields.io/badge/LANG%20Python-3178c6?style=for-the-badge" alt="LANG Python" />
<img src="https://img.shields.io/badge/STARS%200-eab308?style=for-the-badge" alt="STARS 0" />
<img src="https://img.shields.io/badge/LICENSE%20MIT-22c55e?style=for-the-badge" alt="LICENSE MIT" />

<br>

<img src="https://img.shields.io/badge/OPEN%20SOURCE-yes-22c55e?style=for-the-badge&logo=github&logoColor=white" alt="OPEN SOURCE" />
<img src="https://img.shields.io/badge/BUILT%20IN%20PUBLIC-true-6366f1?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="BUILT IN PUBLIC" />
<img src="https://img.shields.io/badge/HANDS%20ON%20LABS-52-0ea5e9?style=for-the-badge&logo=docker&logoColor=white" alt="HANDS ON LABS" />
<img src="https://img.shields.io/badge/DOCUMENTED-yes-14b8a6?style=for-the-badge&logo=markdown&logoColor=white" alt="DOCUMENTED" />

<br>

<b>Riset dan prototipe keamanan berbasis sistem cerdas.</b>

</div>

---
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

[![CI](https://github.com/devarent/keamanan-berbasis-sistem-cerdas/actions/workflows/ci.yml/badge.svg)](https://github.com/devarent/keamanan-berbasis-sistem-cerdas/actions/workflows/ci.yml)

[Contributing](CONTRIBUTING.md) | [Security Policy](SECURITY.md) | [Code of Conduct](CODE_OF_CONDUCT.md)

---

<!-- tech-stack-wall -->
## Tech Stack

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />

</div>

<details>
<summary><b>Full Tech Stack Wall</b></summary>
<br>

<div align="center">

<b>Languages</b><br>
<img src="https://img.shields.io/badge/Rust-dea584?style=for-the-badge&logo=rust&logoColor=black" alt="Rust" />
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white" alt="Swift" />
<img src="https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white" alt="Ruby" />
<img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP" />
<img src="https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white" alt="Lua" />
<img src="https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Shell" />
<br><br>
<b>Frontend &amp; Desktop</b><br>
<img src="https://img.shields.io/badge/Vue-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=black" alt="Vue" />
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white" alt="Svelte" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/Nuxt-00DC82?style=for-the-badge&logo=nuxtdotjs&logoColor=black" alt="Nuxt" />
<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flutter" />
<img src="https://img.shields.io/badge/React%20Native-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React Native" />
<img src="https://img.shields.io/badge/Tauri-FFC131?style=for-the-badge&logo=tauri&logoColor=black" alt="Tauri" />
<img src="https://img.shields.io/badge/Electron-47848F?style=for-the-badge&logo=electron&logoColor=white" alt="Electron" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
<img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white" alt="Sass" />
<img src="https://img.shields.io/badge/Less-1D365D?style=for-the-badge&logo=less&logoColor=white" alt="Less" />
<img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white" alt="Three.js" />
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" alt="jQuery" />
<br><br>
<b>Database &amp; Storage</b><br>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
<img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="Oracle" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
<img src="https://img.shields.io/badge/DuckDB-FFCB00?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB" />
<img src="https://img.shields.io/badge/ClickHouse-FFCC00?style=for-the-badge&logo=clickhouse&logoColor=black" alt="ClickHouse" />
<img src="https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white" alt="Elasticsearch" />
<img src="https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j" />
<img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white" alt="InfluxDB" />
<img src="https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white" alt="Cassandra" />
<img src="https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white" alt="DynamoDB" />
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase" />
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=black" alt="Supabase" />
<img src="https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white" alt="MinIO" />
<br><br>
<b>Messaging &amp; Streaming</b><br>
<img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka" />
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
<img src="https://img.shields.io/badge/RocketMQ-FF6A00?style=for-the-badge&logoColor=white" alt="RocketMQ" />
<img src="https://img.shields.io/badge/Pulsar-188FFF?style=for-the-badge&logo=apachepulsar&logoColor=white" alt="Pulsar" />
<img src="https://img.shields.io/badge/Flink-E6526F?style=for-the-badge&logo=apacheflink&logoColor=white" alt="Flink" />
<br><br>
<b>DevOps &amp; Cloud Native</b><br>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
<img src="https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible" />
<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/GitLab%20CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab CI" />
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
<img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure" />
<img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare" />
<br><br>
<b>Tools &amp; Platforms</b><br>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
<img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
<img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code" />
<img src="https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=vim&logoColor=white" alt="Vim" />
<img src="https://img.shields.io/badge/Tmux-1BB91F?style=for-the-badge&logoColor=white" alt="Tmux" />
<img src="https://img.shields.io/badge/Homebrew-FAB316?style=for-the-badge&logo=homebrew&logoColor=black" alt="Homebrew" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman" />
<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" alt="Figma" />
<img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white" alt="Maven" />
<img src="https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white" alt="CMake" />

</div>
</details>

<div align="center">
<sub>Hands-on engineering, built and documented in the open.</sub>
</div>