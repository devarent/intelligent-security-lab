# BAB III
# METODOLOGI PENELITIAN

## 3.1 Tahapan Penelitian

Penelitian ini dilakukan dengan mengikuti tahapan yang terstruktur untuk memastikan ketepatan dan kevalidan hasil. Tahapan penelitian dapat dilihat pada Gambar 3.1 dan dijelaskan sebagai berikut:

1. **Studi Literatur**: Mengumpulkan dan mempelajari literatur terkait keamanan siber, machine learning, algoritma yang digunakan, dan dataset yang relevan.

2. **Pengumpulan Data**: Mengunduh dan menyiapkan dataset dari berbagai sumber publik yang akan digunakan dalam penelitian.

3. **Preprocessing Data**: Melakukan pembersihan, normalisasi, feature engineering, dan penanganan class imbalance pada dataset.

4. **Perancangan Model**: Mendesain arsitektur dan parameter untuk setiap model machine learning yang akan diimplementasikan.

5. **Implementasi Model**: Menulis kode program untuk mengimplementasikan setiap model machine learning.

6. **Pelatihan Model**: Melatih setiap model menggunakan data yang telah dipreprocessing.

7. **Evaluasi Model**: Mengevaluasi kinerja setiap model menggunakan metrik evaluasi yang sesuai.

8. **Analisis Komparatif**: Membandingkan kinerja berbagai model yang diimplementasikan.

9. **Pengembangan Dashboard**: Membangun dashboard web untuk visualisasi hasil dan pemantauan ancaman.

10. **Dokumentasi dan Pembahasan**: Mendokumentasikan hasil dan melakukan pembahasan mendalam.

## 3.2 Pengumpulan Data

### 3.2.1 Sumber Dataset

Dataset yang digunakan dalam penelitian ini diperoleh dari sumber-sumber publik yang terpercaya:

1. **CIC-IDS2017**: Diunduh dari Canadian Institute for Cybersecurity (https://www.unb.ca/cic/datasets/ids-2017.html)
2. **CIC-IDS2018**: Diunduh dari Canadian Institute for Cybersecurity (https://www.unb.ca/cic/datasets/ids-2018.html)
3. **CIC-DDoS2019**: Diunduh dari Canadian Institute for Cybersecurity (https://www.unb.ca/cic/datasets/ddos-2019.html)
4. **CIC-BCCC-NRC TabularIoTAttack-2024**: Diunduh dari Canadian Institute for Cybersecurity
5. **MalNet-Image**: Diunduh dari repository publik MalNet
6. **CyberLLMInstruct**: Diunduh dari repository publik untuk LLM fine-tuning

### 3.2.2 Deskripsi Dataset

**CIC-IDS2017 dan CIC-IDS2018**
- Ukuran: Berbagai file CSV dengan fitur yang diekstrak dari traffic jaringan
- Fitur: 78-80 fitur yang mencakup statistik flow, packet, dan header
- Label: Binary (normal/attack) dan multi-class (jenis serangan spesifik)
- Jumlah sampel: Ratusan ribu hingga jutaan records

**CIC-DDoS2019**
- Fokus: Berbagai jenis DDoS attacks
- Fitur: Fitur statistik traffic jaringan
- Label: Normal dan berbagai jenis DDoS attacks

**CIC-BCCC-NRC TabularIoTAttack-2024**
- Fokus: Serangan pada perangkat IoT
- Format: Tabular data siap digunakan
- Label: Berbagai jenis serangan IoT

**MalNet-Image**
- Format: Citra (gambar) dari binary malware
- Ukuran: Subset dari 1,2 juta gambar malware
- Kelas: Berbagai keluarga malware
- Dimensi citra: Bervariasi, akan di-resize ke ukuran standar

**CyberLLMInstruct**
- Format: JSON dengan pasangan instruction-response
- Konten: Tugas keamanan siber
- Ukuran: 54.928 pasangan

### 3.2.3 Proses Pengunduhan dan Validasi

1. Dataset diunduh dari sumber resmi menggunakan protokol HTTPS untuk memastikan integritas.
2. Integritas file divalidasi menggunakan checksum jika tersedia.
3. Dataset diekstrak jika dalam format terkompresi (zip, tar.gz).
4. Struktur dataset diperiksa untuk memastikan konsistensi format.
5. Sampel data diperiksa secara manual untuk memverifikasi kualitas.

## 3.3 Preprocessing Data

### 3.3.1 Pembersihan Data (Data Cleaning)

Langkah-langkah pembersihan data yang dilakukan:

1. **Penanganan Missing Values**
   - Mengidentifikasi kolom dengan missing values
   - Jika missing values < 5%: Menghapus baris dengan missing values
   - Jika missing values 5-20%: Mengisi dengan mean/median (numerik) atau mode (kategorikal)
   - Jika missing values > 20%: Menghapus kolom tersebut

2. **Penghapusan Duplikasi**
   - Mengidentifikasi baris yang duplikat
   - Menghapus duplikat untuk menghindari bias dalam pelatihan

3. **Penanganan Outlier**
   - Mengidentifikasi outlier menggunakan IQR (Interquartile Range) atau Z-score
   - Outlier ekstrem dihapus atau dicapping ke batas wajar
   - Untuk dataset deteksi anomali, outlier mungkin merupakan data serangan yang valid

4. **Validasi Tipe Data**
   - Memastikan tipe data sesuai (numerik, kategorikal, datetime)
   - Konversi tipe data jika diperlukan

### 3.3.2 Normalisasi dan Standarisasi

**Untuk dataset jaringan (CIC-IDS):**
1. Identifikasi fitur numerik yang perlu dinormalisasi
2. Terapkan StandardScaler (Z-score normalization) untuk fitur dengan distribusi mendekati normal
3. Terapkan MinMaxScaler untuk fitur dengan distribusi tidak normal
4. Fitur yang sudah dalam skala 0-1 atau binary tidak perlu dinormalisasi

**Untuk dataset citra (MalNet-Image):**
1. Normalisasi pixel values ke rentang [0, 1] dengan membagi dengan 255
2. Atau normalisasi ke mean=0, std=1 menggunakan ImageNet statistics untuk transfer learning

### 3.3.3 Feature Engineering

Feature engineering yang dilakukan meliputi:

1. **Time-based Features**
   - Ekstraksi hour, day, month dari timestamp
   - Encoding cyclic features (hour, day of week) menggunakan sin/cos transformasi

2. **Statistical Features**
   - Rolling statistics (mean, std, min, max) dalam window waktu
   - Lag features untuk data time series

3. **Ratio Features**
   - Rasio antara fitur yang relevan (misalnya: forward/backward packets ratio)
   - Rate-based features (packets per second, bytes per second)

4. **Aggregation Features**
   - Agregasi berdasarkan source/destination IP dalam window waktu
   - Count features untuk aktivitas spesifik

### 3.3.4 Encoding Data Kategorikal

1. **One-Hot Encoding**
   - Digunakan untuk fitur kategorikal dengan cardinality rendah (< 10 kategori)
   - Contoh: Protocol type (TCP, UDP, ICMP)

2. **Label Encoding**
   - Digunakan untuk fitur kategorikal dengan cardinality tinggi atau ordinal
   - Contoh: Flag values

3. **Target Encoding**
   - Digunakan untuk kategorikal dengan cardinality sangat tinggi
   - Dengan cross-validation untuk menghindari data leakage

### 3.3.5 Handling Class Imbalance

Teknik yang digunakan untuk menangani class imbalance:

1. **SMOTE (Synthetic Minority Over-sampling Technique)**
   - Digunakan untuk dataset dengan imbalance moderate
   - Membuat sampel sintetis untuk kelas minoritas
   - Parameter: k_neighbors=5, sampling_strategy='auto'

2. **SMOTE-ENN**
   - Kombinasi oversampling (SMOTE) dan undersampling (ENN)
   - Digunakan untuk dataset dengan imbalance yang lebih tinggi

3. **Class Weights**
   - Menggunakan class weights dalam model yang mendukungnya
   - Bobot dihitung sebagai inverse dari class frequency

4. **Ensemble Methods**
   - Menggunakan algoritma yang inherently robust terhadap imbalance (Random Forest, XGBoost)

### 3.3.6 Splitting Data

Dataset dibagi menjadi tiga bagian:

1. **Training Set**: 70% dari data - untuk melatih model
2. **Validation Set**: 15% dari data - untuk hyperparameter tuning dan model selection
3. **Test Set**: 15% dari data - untuk evaluasi final model

Splitting dilakukan dengan stratified sampling untuk mempertahankan distribusi kelas. Untuk data time series, splitting dilakukan secara temporal (train pada data awal, test pada data akhir).

## 3.4 Perancangan Model Machine Learning

### 3.4.1 Model Deteksi Anomali dengan Isolation Forest

**Arsitektur:**
- Algorithm: Isolation Forest
- n_estimators: 100 (jumlah isolation trees)
- max_samples: 'auto' (256)
- contamination: 0.1 (proporsi anomali yang diharapkan)
- max_features: 1.0 (semua fitur digunakan)
- bootstrap: False
- n_jobs: -1 (gunakan semua CPU cores)
- random_state: 42 (untuk reproducibility)

**Cara Kerja:**
1. Algoritma membangun 100 isolation trees secara acak
2. Setiap tree mempartisi data dengan memilih fitur dan split point secara acak
3. Path length setiap data point dihitung
4. Anomali memiliki path length yang lebih pendek
5. Skor anomali dihitung berdasarkan rata-rata path length

**Parameter Tuning:**
- n_estimators: [50, 100, 200]
- contamination: [0.01, 0.05, 0.1, 0.2]
- max_samples: [64, 128, 256, 'auto']

### 3.4.2 Model Klasifikasi Malware dengan CNN

**Arsitektur CNN:**
```
Input Layer: (64, 64, 3) - citra malware resize ke 64x64

Conv2D(32, (3,3), activation='relu')
MaxPooling2D((2,2))
BatchNormalization()
Dropout(0.25)

Conv2D(64, (3,3), activation='relu')
MaxPooling2D((2,2))
BatchNormalization()
Dropout(0.25)

Conv2D(128, (3,3), activation='relu')
MaxPooling2D((2,2))
BatchNormalization()
Dropout(0.25)

Flatten()

Dense(256, activation='relu')
BatchNormalization()
Dropout(0.5)

Dense(num_classes, activation='softmax')
```

**Hyperparameters:**
- Optimizer: Adam dengan learning_rate=0.001
- Loss function: Categorical Crossentropy
- Batch size: 32
- Epochs: 50 dengan early stopping
- Callbacks: EarlyStopping(patience=10), ModelCheckpoint, ReduceLROnPlateau

**Data Augmentation:**
- Rotation: 10 derajat
- Width shift: 10%
- Height shift: 10%
- Horizontal flip
- Zoom: 10%

### 3.4.3 Model Analisis Relasional dengan GCN

**Arsitektur GCN:**
```
Input Layer: Node features dan adjacency matrix

GCN Layer 1 (hidden_dim=128)
Activation: ReLU
Dropout: 0.5

GCN Layer 2 (hidden_dim=64)
Activation: ReLU
Dropout: 0.5

Global Mean Pooling

Dense(32, activation='relu')
Dropout(0.5

Dense(num_classes, activation='softmax')
```

**Graph Construction:**
- Node: Entitas (file, proses, user, endpoint)
- Edge: Relasi antar entitas (akses file, koneksi jaringan, dll.)
- Node features: Fitur dari setiap entitas
- Adjacency matrix: Representasi konektivitas graph

**Hyperparameters:**
- Learning rate: 0.01
- Weight decay: 5e-4
- Hidden dimensions: [128, 64]
- Dropout: 0.5
- Epochs: 200

### 3.4.4 Model Ensemble

**Struktur Ensemble:**
Ensemble menggunakan stacking method dengan tiga base models dan satu meta-model.

**Base Models:**
1. **Random Forest**
   - n_estimators: 200
   - max_depth: 20
   - min_samples_split: 5
   - class_weight: 'balanced'

2. **XGBoost**
   - n_estimators: 200
   - max_depth: 6
   - learning_rate: 0.1
   - subsample: 0.8
   - colsample_bytree: 0.8
   - scale_pos_weight: untuk class imbalance

3. **LightGBM**
   - n_estimators: 200
   - max_depth: 6
   - learning_rate: 0.1
   - num_leaves: 31
   - is_unbalance: True

**Meta-Model:**
- Logistic Regression dengan regularization
- Dilatih pada predictions dari base models (5-fold cross-validation)

**Alternatif: Voting Classifier**
- Hard voting: Majority vote dari base models
- Soft voting: Weighted average dari probability predictions

### 3.4.5 Model LLM untuk Intelijen Ancaman

**Base Model:**
- Menggunakan pre-trained LLM (misalnya BERT-base atau GPT-2)

**Fine-tuning Strategy:**
1. **Dataset Preparation**
   - Menggunakan CyberLLMInstruct dengan 54.928 instruction-response pairs
   - Split: 80% training, 10% validation, 10% test

2. **Fine-tuning Configuration**
   - Learning rate: 2e-5
   - Batch size: 16
   - Epochs: 3-5 (untuk menghindari overfitting)
   - Max sequence length: 512
   - Warmup steps: 10% dari total steps

3. **Training Approach**
   - Instruction tuning dengan format prompt-response
   - Loss function: Cross-entropy pada token predictions
   - Optimizer: AdamW dengan weight decay

4. **Inference**
   - Input: Instruction tentang analisis keamanan siber
   - Output: Response dari model yang di-fine-tune
   - Temperature: 0.7 untuk generation

## 3.5 Pelatihan dan Evaluasi Model

### 3.5.1 Pelatihan Model

**Proses Pelatihan:**
1. Setiap model dilatih secara terpisah menggunakan training set
2. Validation set digunakan untuk:
   - Hyperparameter tuning
   - Model selection
   - Early stopping untuk mencegah overfitting
3. Training progress dimonitor dengan metrics:
   - Loss per epoch
   - Accuracy per epoch
   - Validation loss dan accuracy

**Cross-Validation:**
- Untuk model ensemble, digunakan 5-fold stratified cross-validation
- Memastikan generalisasi model yang baik

**Saving Models:**
- Model terbaik disimpan dalam format:
  - Scikit-learn: Joblib (.pkl)
  - Deep Learning (Keras/PyTorch): HDF5 (.h5) atau (.pt)
  - LLM: HuggingFace Transformers format

### 3.5.2 Evaluasi Model

Evaluasi dilakukan pada test set yang tidak pernah dilihat selama pelatihan.

## 3.6 Metrik Evaluasi

### 3.6.1 Metrik untuk Klasifikasi

**1. Accuracy**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```
Persentase prediksi yang benar. Berguna untuk balanced dataset.

**2. Precision**
```
Precision = TP / (TP + FP)
```
Persentase prediksi positif yang benar. Penting untuk meminimalkan false positives.

**3. Recall (Sensitivity)**
```
Recall = TP / (TP + FN)
```
Persentase kasus positif yang terdeteksi. Penting untuk meminimalkan false negatives.

**4. F1-Score**
```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```
Harmonic mean dari precision dan recall. Memberikan balance antara keduanya.

**5. Specificity**
```
Specificity = TN / (TN + FP)
```
Persentase kasus negatif yang terdeteksi dengan benar.

**6. ROC-AUC**
- Area di bawah Receiver Operating Characteristic curve
- Mengukur trade-off antara TPR dan FPR
- Nilai 0.5 = random, 1.0 = perfect

**7. Confusion Matrix**
- Visualisasi TP, TN, FP, FN untuk setiap kelas
- Membantu menganalisis error types

### 3.6.2 Metrik untuk Deteksi Anomali

**1. Detection Rate**
Persentase anomali yang berhasil dideteksi.

**2. False Positive Rate**
Persentase data normal yang salah diklasifikasikan sebagai anomali.

**3. Precision@k**
Precision pada top-k anomali dengan skor tertinggi.

### 3.6.3 Metrik untuk LLM

**1. BLEU Score**
Mengukur similarity dengan reference text.

**2. ROUGE Score**
Mengukur recall pada n-gram overlap.

**3. Perplexity**
Mengukur seberapa "terkejut" model terhadap test data.

**4. Human Evaluation**
Kualitas dan relevansi response untuk tugas keamanan siber.

## 3.7 Pengembangan Dashboard Web

### 3.7.1 Teknologi yang Digunakan

**Frontend:**
- Framework: React.js atau Vue.js
- Library Charting: Chart.js atau D3.js
- UI Framework: Bootstrap atau Tailwind CSS
- State Management: Redux atau Vuex

**Backend:**
- Framework: Flask (Python) atau FastAPI
- API: RESTful API untuk komunikasi frontend-backend
- Database: SQLite atau PostgreSQL untuk menyimpan hasil prediksi

**Deployment:**
- Web Server: Nginx atau Apache
- Containerization: Docker (opsional)

### 3.7.2 Fitur Dashboard

**1. Real-time Monitoring**
- Visualisasi traffic jaringan live
- Alert untuk anomali yang terdeteksi
- Time series plot untuk metric jaringan

**2. Model Performance Dashboard**
- Accuracy, precision, recall, F1-score per model
- Confusion matrix interactive
- ROC curves
- Feature importance plots

**3. Threat Intelligence**
- Display hasil analisis LLM
- Summary ancaman yang terdeteksi
- Rekomendasi mitigasi

**4. Historical Analysis**
- Timeline serangan
- Trend analysis
- Comparison antar periode

**5. Export Functionality**
- Export hasil ke CSV/PDF
- Generate laporan otomatis

### 3.7.3 Arsitektur Dashboard

```
[Frontend - React]
    ↓ API Calls
[Backend - Flask/FastAPI]
    ↓
[ML Models - Loaded from disk]
    ↓
[Database - SQLite/PostgreSQL]
```

Backend menyediakan endpoint untuk:
- /api/predict - Menerima data dan mengembalikan prediksi
- /api/performance - Mengembalikan metrik kinerja model
- /api/history - Mengembalikan riwayat prediksi
- /api/threat-intel - Mengembalikan analisis LLM

## 3.8 Alur Penelitian

Alur penelitian secara keseluruhan dapat dilihat pada diagram berikut:

```
[Mulai]
   ↓
[Studi Literatur]
   ↓
[Pengumpulan Dataset]
   ↓
[Preprocessing Data]
   ├── Data Cleaning
   ├── Normalisasi
   ├── Feature Engineering
   ├── Encoding
   └── Handling Class Imbalance
   ↓
[Splitting Data]
   ├── Training Set (70%)
   ├── Validation Set (15%)
   └── Test Set (15%)
   ↓
[Perancangan Model]
   ├── Isolation Forest
   ├── CNN
   ├── GCN
   ├── Ensemble
   └── LLM
   ↓
[Implementasi Model]
   ↓
[Pelatihan Model]
   ↓
[Evaluasi Model]
   ├── Accuracy
   ├── Precision
   ├── Recall
   ├── F1-Score
   └── ROC-AUC
   ↓
[Analisis Komparatif]
   ↓
[Pengembangan Dashboard]
   ↓
[Dokumentasi & Pembahasan]
   ↓
[Selesai]
```

Alur ini memastikan bahwa penelitian dilakukan secara sistematis dan setiap tahap didokumentasi dengan baik.
