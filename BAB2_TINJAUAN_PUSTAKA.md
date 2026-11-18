# BAB II
# TINJAUAN PUSTAKA

## 2.1 Keamanan Siber

Keamanan siber (cybersecurity) adalah praktik melindungi sistem, jaringan, dan program dari serangan digital. Serangan siber ini biasanya bertujuan untuk mengakses, mengubah, atau menghancurkan informasi sensitif, memeras uang dari pengguna, atau mengganggu operasi bisnis normal. Dalam era digital saat ini, keamanan siber menjadi aspek kritis yang tidak dapat dipisahkan dari operasi organisasi, baik sektor publik maupun swasta.

### 2.1.1 Jenis-Jenis Serangan Siber

Serangan siber dapat diklasifikasikan menjadi beberapa kategori utama:

**1. Distributed Denial of Service (DDoS)**
DDoS adalah serangan yang bertujuan untuk membuat layanan atau jaringan tidak dapat diakses dengan membanjiri lalu lintas dengan request yang sangat besar. Serangan ini dapat berupa volumetric attacks yang membanjiri bandwidth jaringan, protocol attacks yang mengeksploitasi kelemahan protokol jaringan, atau application layer attacks yang menargetkan aplikasi web spesifik.

**2. Malware**
Malware (malicious software) adalah perangkat lunak yang dirancang untuk merusak atau mengganggu sistem komputer. Jenis-jenis malware meliputi:
- Virus: program yang menempel pada file yang sah dan menyebar ketika file tersebut dieksekusi
- Worms: program yang dapat mereplikasi diri dan menyebar melalui jaringan tanpa interaksi pengguna
- Trojans: program yang menyamar sebagai perangkat lunak sah untuk menipu pengguna menginstalnya
- Ransomware: malware yang mengenkripsi data korban dan menuntut pembayaran tebusan
- Spyware: program yang mengumpulkan informasi pengguna tanpa sepengetahuan

**3. Phishing**
Phishing adalah serangan social engineering yang mencoba memperoleh informasi sensitif seperti username, password, dan detail kartu kredit dengan menyamar sebagai entitas yang terpercaya melalui email, SMS, atau website palsu.

**4. Man-in-the-Middle (MitM) Attack**
Serangan ini terjadi ketika penyerang mencegat komunikasi antara dua pihak untuk memata-matai atau memodifikasi data yang ditransmisikan.

**5. SQL Injection**
SQL Injection adalah serangan yang memanfaatkan kerentanan aplikasi web untuk memanipulasi database backend, memungkinkan penyerang mengakses, memodifikasi, atau menghapus data sensitif.

**6. Zero-Day Exploits**
Serangan yang memanfaatkan kerentanan yang belum diketahui oleh vendor perangkat lunak dan belum memiliki patch atau perbaikan.

### 2.1.2 Tantangan Deteksi Serangan Siber

Deteksi serangan siber menghadapi beberapa tantangan utama:

**1. Volume Data yang Besar**
Jaringan modern menghasilkan data log dan traffic dalam volume yang sangat besar, membuat analisis manual menjadi tidak praktis. Security Operation Center (SOC) harus memproses ribuan atau bahkan jutaan events per hari.

**2. Evolusi Serangan yang Cepat**
Penyerang terus mengembangkan teknik baru dan memodifikasi serangan yang ada untuk menghindari deteksi oleh sistem keamanan yang ada. Signature-based detection sering gagal mengenali varian baru.

**3. False Positives**
Sistem deteksi yang terlalu sensitif dapat menghasilkan banyak false positives, menyebabkan alert fatigue di kalangan analis keamanan dan mengurangi efektivitas sistem.

**4. Class Imbalance**
Dalam dataset keamanan siber, kasus serangan (anomali) jauh lebih sedikit dibandingkan dengan aktivitas normal, menciptakan class imbalance yang menjadi tantangan dalam pelatihan model machine learning.

**5. Complex Patterns**
Serangan modern sering melibatkan pola yang kompleks dan multi-stage, yang sulit dideteksi dengan rule-based system sederhana.

## 2.2 Machine Learning

Machine learning adalah cabang kecerdasan buatan yang memberikan kemampuan kepada sistem untuk belajar dari data tanpa diprogram secara eksplisit untuk setiap tugas. Sistem machine learning menggunakan algoritma untuk mengidentifikasi pola dalam data dan membuat prediksi atau keputusan berdasarkan pola tersebut.

### 2.2.1 Supervised Learning

Supervised learning adalah pendekatan machine learning di mana model dilatih menggunakan data yang sudah diberi label (labeled data). Model belajar memetakan input ke output yang diinginkan berdasarkan contoh-contoh yang telah diberikan. Contoh algoritma supervised learning meliputi:

- **Decision Trees**: Memecah ruang fitur menjadi region-region berdasarkan aturan if-then
- **Random Forest**: Ensemble dari decision trees yang dilatih pada subset data dan fitur yang berbeda
- **Support Vector Machines (SVM)**: Mencari hyperplane optimal yang memisahkan kelas-kelas
- **Logistic Regression**: Model linear untuk klasifikasi biner
- **Neural Networks**: Model terinspirasi biologi dengan lapisan neuron yang saling terhubung

### 2.2.2 Unsupervised Learning

Unsupervised learning digunakan ketika data tidak memiliki label. Model harus menemukan struktur atau pola dalam data secara mandiri. Contoh algoritma unsupervised learning meliputi:

- **K-Means Clustering**: Mengelompokkan data ke dalam k cluster berdasarkan jarak ke centroid
- **Hierarchical Clustering**: Membangun hierarki cluster dengan cara top-down atau bottom-up
- **DBSCAN**: Density-based clustering yang dapat menemukan cluster dengan bentuk arbitrer
- **Principal Component Analysis (PCA)**: Teknik reduksi dimensi untuk mengurangi kompleksitas data
- **Autoencoders**: Neural networks yang dilatih untuk merekonstruksi input, digunakan untuk deteksi anomali

### 2.2.3 Deep Learning

Deep learning adalah subset machine learning yang menggunakan neural networks dengan banyak lapisan (deep neural networks). Deep learning sangat efektif untuk tugas-tugas yang melibatkan data kompleks seperti citra, teks, dan audio. Arsitektur deep learning yang umum meliputi:

- **Convolutional Neural Networks (CNN)**: Dirancang khusus untuk data dengan struktur spasial seperti citra
- **Recurrent Neural Networks (RNN)**: Cocok untuk data sekuensial seperti teks dan time series
- **Long Short-Term Memory (LSTM)**: Variasi RNN yang dapat menangani long-term dependencies
- **Transformers**: Arsitektur berbasis attention mechanism yang menjadi standar untuk NLP
- **Graph Neural Networks (GNN)**: Dirancang untuk data berbasis graph

## 2.3 Algoritma Machine Learning untuk Keamanan Siber

### 2.3.1 Isolation Forest

Isolation Forest adalah algoritma unsupervised learning yang dikembangkan khusus untuk deteksi anomali. Algoritma ini bekerja dengan prinsip bahwa anomali lebih mudah diisolasi daripada data normal karena mereka bersifat langka dan berbeda.

**Cara Kerja:**
1. Algoritma membangun beberapa isolation trees (iTrees) dengan cara secara acak memilih fitur dan split point
2. Setiap iTree mempartisi data secara rekursif sampai setiap data point terisolasi
3. Depth rata-rata suatu data point dalam iTree dihitung sebagai path length
4. Anomali biasanya memiliki path length yang lebih pendek karena mudah diisolasi
5. Skor anomali dihitung berdasarkan path length rata-rata di semua iTrees

**Kelebihan:**
- Efisien secara komputasi dengan kompleksitas O(n)
- Tidak memerlukan label data
- Efektif untuk deteksi outlier dalam data berdimensi tinggi
- Skalabel untuk dataset besar

**Keterbatasan:**
- Sensitif terhadap parameter n_estimators dan contamination
- Mungkin kurang efektif jika anomali memiliki pola yang kompleks
- Tidak memberikan interpretasi yang mudah tentang mengapa suatu data dianggap anomali

### 2.3.2 Convolutional Neural Networks (CNN)

CNN adalah arsitektur deep learning yang sangat efektif untuk tugas-tugas yang melibatkan data dengan struktur spasial seperti citra. CNN menggunakan operasi konvolusi untuk mengekstrak fitur dari data secara hierarkis.

**Komponen Utama CNN:**
1. **Convolutional Layer**: Mengaplikasikan filter (kernel) ke input untuk mengekstrak fitur lokal
2. **Pooling Layer**: Mengurangi dimensi spasial dengan downsampling (max pooling, average pooling)
3. **Activation Function**: Menambahkan non-linearity (ReLU, sigmoid, tanh)
4. **Fully Connected Layer**: Layer terakhir untuk klasifikasi berdasarkan fitur yang diekstrak

**Kelebihan:**
- Mampu mengekstrak fitur secara otomatis tanpa feature engineering manual
- Parameter sharing mengurangi jumlah parameter yang perlu dipelajari
- Translational invariance: mengenali pola di berbagai posisi
- Sangat efektif untuk klasifikasi citra dan tugas computer vision lainnya

**Aplikasi dalam Keamanan Siber:**
- Klasifikasi malware berbasis citra (malware visualization)
- Deteksi phishing berbasis screenshot website
- Analisis traffic jaringan yang direpresentasikan sebagai citra

### 2.3.3 Graph Convolutional Networks (GCN)

GCN adalah jenis Graph Neural Network (GNN) yang dirancang untuk data berbasis graph. Dalam konteks keamanan siber, graph dapat merepresentasikan relasi antar entitas seperti file, proses, user, dan endpoint.

**Cara Kerja:**
1. Node dalam graph merepresentasikan entitas (misalnya file, proses)
2. Edge merepresentasikan relasi antar entitas (misalnya file yang diakses oleh proses)
3. GCN menggunakan operasi konvolusi pada graph untuk mengagregasi informasi dari node tetangga
4. Setiap layer GCN mengupdate representasi node berdasarkan informasi dari tetangganya
5. Setelah beberapa layer, setiap node memiliki representasi yang menggabungkan informasi dari graph lokalnya

**Kelebihan:**
- Dapat menangkap struktur relasional yang kompleks
- Sesuai untuk analisis malware dan sistem di mana relasi antar entitas penting
- Dapat mengidentifikasi pola anomali dalam graph structure

**Aplikasi dalam Keamanan Siber:**
- Analisis behavior graph malware
- Deteksi lateral movement dalam jaringan
- Identifikasi botnet berdasarkan struktur komunikasi

### 2.3.4 Ensemble Methods

Ensemble methods menggabungkan prediksi dari beberapa model untuk meningkatkan kinerja secara keseluruhan. Prinsip dasarnya adalah bahwa kombinasi beberapa model yang cukup baik dapat menghasilkan prediksi yang lebih baik daripada model tunggal.

**Jenis Ensemble Methods:**

1. **Bagging (Bootstrap Aggregating)**
   - Melatih beberapa model pada subset data yang berbeda (dengan sampling with replacement)
   - Menggabungkan prediksi dengan voting (klasifikasi) atau averaging (regresi)
   - Contoh: Random Forest

2. **Boosting**
   - Melatih model secara berurutan, di mana setiap model baru fokus pada error model sebelumnya
   - Memberikan bobot lebih besar pada instance yang sulit diklasifikasikan
   - Contoh: AdaBoost, XGBoost, LightGBM

3. **Stacking**
   - Menggabungkan beberapa model base dengan meta-model yang mempelajari cara menggabungkan prediksi mereka
   - Meta-model dilatih pada output dari base models

4. **Voting Classifier**
   - Menggabungkan prediksi dari beberapa model menggunakan majority voting (hard voting) atau weighted average (soft voting)

**Kelebihan:**
- Mengurangi overfitting
- Meningkatkan generalisasi
- Dapat menggabungkan kelebihan berbagai algoritma berbeda
- Sering menghasilkan kinerja yang lebih stabil

### 2.3.5 Large Language Models (LLM)

LLM adalah model neural networks dengan miliaran parameter yang dilatih pada corpus teks yang sangat besar. Model seperti GPT, BERT, dan variannya telah menunjukkan kemampuan luar biasa dalam berbagai tugas NLP.

**Dalam Konteks Keamanan Siber:**
LLM dapat digunakan untuk:
- Analisis intelijen ancaman (Cyber Threat Intelligence)
- Interpretasi log dan deskripsi serangan
- Pembuatan laporan keamanan otomatis
- Analisis teks dalam phishing emails
- Fine-tuning untuk tugas spesifik keamanan menggunakan dataset seperti CyberLLMInstruct

**CyberLLMInstruct:**
- Dataset berisi 54.928 pasangan instruction-response untuk tugas keamanan siber
- Mencakup analisis malware, phishing, dan ancaman zero-day
- Berguna untuk fine-tuning LLM agar memahami konteks keamanan siber

## 2.4 Dataset Keamanan Siber

Dataset berkualitas adalah fondasi penting untuk penelitian machine learning dalam keamanan siber. Canadian Institute for Cybersecurity (CIC) dan berbagai lembaga lainnya telah menyediakan dataset publik yang komprehensif.

### 2.4.1 CIC-IDS2017

CIC-IDS2017 adalah dataset intrusi jaringan yang dikembangkan oleh Canadian Institute for Cybersecurity. Dataset ini berisi lalu lintas jaringan yang mencakup aktivitas normal dan berbagai jenis serangan.

**Karakteristik:**
- Ukuran dataset: sekitar 80 GB data PCAP
- Fitur: 78 fitur yang diekstrak dari traffic jaringan
- Jenis serangan: DDoS, DoS, brute force, infiltration, botnet, web attack
- Durasi: 5 hari capture traffic
- Label: Binary (normal/attack) dan multi-class (jenis serangan)

**Kelebihan:**
- Traffic jaringan realistis
- Serangan dengan berbagai intensitas
- Fitur statistik yang komprehensif
- Documentation yang baik

### 2.4.2 CIC-IDS2018

CIC-IDS2018 adalah dataset yang dikembangkan setelah CIC-IDS2017 dengan peningkatan dan skenario serangan yang lebih beragam.

**Karakteristik:**
- Fitur: 80 fitur statistik dari traffic jaringan
- Jenis serangan: brute force, heartbleed, botnet, DoS, DDoS, web attack, infiltration
- Durasi: 10 hari capture traffic
- Ukuran dataset: lebih besar dari CIC-IDS2017
- Termasuk traffic HTTPS dan HTTP

**Peningkatan dari CIC-IDS2017:**
- Lebih banyak skenario serangan
- Durasi capture yang lebih panjang
- Fitur yang lebih kaya
- Mencakup protocol dan scenario yang lebih modern

### 2.4.3 CIC-DDoS2019

Dataset yang berfokus khusus pada berbagai jenis DDoS attacks.

**Karakteristik:**
- Jenis serangan: Reflective DDoS (LDAP, DNS, MSSQL, UDP, SYN, NTP, SSDP)
- Termasuk traffic normal dan traffic serangan
- Fitur: Fitur statistik dari traffic jaringan
- Fokus pada serangan volumetrik dan reflective

**Aplikasi:**
- Penelitian deteksi DDoS
- Pengembangan sistem mitigasi DDoS
- Analisis pola traffic DDoS

### 2.4.4 CIC-BCCC-NRC TabularIoTAttack-2024

Dataset berbasis tabular yang berfokus pada serangan terhadap perangkat IoT.

**Karakteristik:**
- Fokus: Serangan IoT (Internet of Things)
- Format: Tabular data yang siap digunakan untuk ML
- Berlabel: Labeled dataset untuk supervised learning
- Traffic jaringan realistis untuk environment IoT
- Berbagai jenis serangan IoT spesifik

**Aplikasi:**
- Penelitian keamanan IoT
- Deteksi anomali pada perangkat IoT
- Pengembangan sistem keamanan untuk smart home dan smart city

### 2.4.5 MalNet-Image

Dataset besar berbasis computer vision untuk klasifikasi malware.

**Karakteristik:**
- Ukuran: Lebih dari 1,2 juta gambar malware
- Representasi: Biner malware yang dikonversi menjadi citra
- Kelas: Berbagai keluarga malware
- Keuntungan: Tidak memerlukan feature engineering konvensional

**Aplikasi:**
- Klasifikasi malware berbasis citra
- Deteksi malware menggunakan computer vision
- Riset metode deteksi malware baru

### 2.4.6 CyberLLMInstruct

Dataset untuk fine-tuning LLM dalam konteks keamanan siber.

**Karakteristik:**
- Ukuran: 54.928 pasangan instruction-response
- Konten: Tugas keamanan siber (malware analysis, phishing, zero-day threats)
- Format: Instruction-following dataset
- Berguna untuk: Fine-tuning LLM dan evaluasi keamanan model

**Aplikasi:**
- Pelatihan LLM untuk konteks keamanan siber
- Analisis intelijen ancaman otomatis
- Pembuatan respon keamanan otomatis

## 2.5 Preprocessing Data

Preprocessing data adalah langkah kritis dalam machine learning yang memastikan kualitas dan kesiapan data untuk pelatihan model.

### 2.5.1 Normalisasi dan Standarisasi

**Normalisasi (Min-Max Scaling):**
- Mengubah nilai fitur ke rentang [0, 1]
- Formula: X_normalized = (X - X_min) / (X_max - X_min)
- Cocok untuk data dengan distribusi tidak normal
- Sensitif terhadap outlier

**Standarisasi (Z-Score Scaling):**
- Mengubah fitur sehingga memiliki mean=0 dan standard deviation=1
- Formula: X_standardized = (X - μ) / σ
- Cocok untuk data dengan distribusi normal (Gaussian)
- Lebih robust terhadap outlier

**Penting dalam Keamanan Siber:**
- Fitur dalam dataset keamanan siber memiliki skala yang sangat berbeda (misalnya: jumlah bytes vs jumlah packets)
- Normalisasi memastikan model tidak bias ke fitur dengan skala besar
- Meningkatkan konvergensi pelatihan model

### 2.5.2 Feature Engineering

Feature engineering adalah proses menciptakan fitur baru dari data mentah untuk meningkatkan kinerja model.

**Teknik Feature Engineering:**
1. **Statistical Features**: Mean, median, variance, skewness, kurtosis
2. **Time-based Features**: Hour of day, day of week, time since last event
3. **Aggregation Features**: Count, sum, average dalam window waktu
4. **Ratio Features**: Rasio antara dua fitur (misalnya: failed login / total login)
5. **Encoding**: One-hot encoding, label encoding untuk data kategorikal

**Contoh dalam Keamanan Siber:**
- Rasio login gagal vs berhasil untuk deteksi brute force
- Jumlah koneksi dalam window waktu untuk deteksi DDoS
- Protocol distribution untuk identifikasi pola anomali

### 2.5.3 Handling Class Imbalance

Class imbalance adalah masalah umum dalam dataset keamanan siber di mana data serangan jauh lebih sedikit daripada data normal.

**Teknik Penanganan:**

1. **Oversampling Minority Class**
   - SMOTE (Synthetic Minority Over-sampling Technique): Membuat sampel sintetis untuk kelas minoritas
   - Random oversampling: Menduplikasi sampel kelas minoritas

2. **Undersampling Majority Class**
   - Random undersampling: Menghapus sampel kelas mayoritas secara acak
   - Tomek links: Menghapus sampel yang ambigu

3. **Hybrid Methods**
   - SMOTE + Tomek links
   - SMOTE + ENN (Edited Nearest Neighbors)

4. **Cost-Sensitive Learning**
   - Memberikan bobot lebih besar pada kelas minoritas dalam loss function
   - Menggunakan class weights dalam model

5. **Ensemble Methods**
   - Bagging dengan balanced samples
   - Balanced Random Forest

### 2.5.4 Encoding Data Kategorikal

Data kategorikal perlu dikonversi ke format numerik agar dapat diproses oleh model machine learning.

**One-Hot Encoding:**
- Membuat kolom biner untuk setiap kategori
- Contoh: Protocol [TCP, UDP, ICMP] → [1,0,0], [0,1,0], [0,0,1]
- Kelebihan: Tidak mengasumsikan ordinal relationship
- Kekurangan: Dapat menyebabkan curse of dimensionality jika kategori banyak

**Label Encoding:**
- Mengassign integer ke setiap kategori
- Contoh: TCP=0, UDP=1, ICMP=2
- Kelebihan: Efisien untuk kategori banyak
- Kekurangan: Mengasumsikan ordinal relationship yang mungkin tidak ada

**Target Encoding:**
- Mengganti kategori dengan mean dari target untuk kategori tersebut
- Berguna untuk kategori dengan cardinality tinggi
- Perlu berhati-hati terhadap data leakage

## 2.6 Penelitian Terdahulu

Berbagai penelitian telah dilakukan untuk menerapkan machine learning dalam deteksi ancaman keamanan siber. Beberapa penelitian relevan meliputi:

**Sharafaldin et al. (2018)**
Mengembangkan dataset CIC-IDS2017 dan mengevaluasi berbagai algoritma machine learning untuk deteksi intrusi jaringan. Hasil menunjukkan bahwa ensemble methods seperti Random Forest dan XGBoost mencapai akurasi tinggi di atas 98% untuk beberapa jenis serangan.

**Vinayakumar et al. (2019)**
Menggunakan Deep Learning dengan CNN dan LSTM untuk deteksi malware. Penelitian menunjukkan bahwa deep learning models dapat mengungguli machine learning tradisional dalam klasifikasi malware.

**Tama et al. (2020)**
Melakukan komparasi berbagai algoritma machine learning pada dataset CIC-IDS2017. Hasil menunjukkan bahwa XGBoost dan LightGBM memberikan kinerja terbaik dengan waktu pelatihan yang relatif cepat.

**Moustafa et al. (2021)**
Mengimplementasikan Isolation Forest untuk deteksi anomali dalam jaringan IoT. Penelitian menunjukkan efektivitas Isolation Forest dalam mendeteksi anomali dengan false positive rate yang rendah.

**Yuan et al. (2022)**
Menggunakan Graph Neural Networks untuk analisis malware. Penelitian menunjukkan bahwa GNN dapat menangkap relasi antar file dan proses untuk deteksi malware yang lebih akurat.

**Abdulrahman et al. (2023)**
Menggunakan LLM yang di-fine-tune untuk analisis intelijen ancaman. Penelitian menunjukkan potensi LLM dalam memberikan analisis interpretatif untuk konteks keamanan siber.

Penelitian-penelitian tersebut menunjukkan bahwa machine learning dan deep learning memberikan kontribusi signifikan dalam meningkatkan deteksi ancaman keamanan siber. Namun, masih terdapat ruang untuk penelitian yang lebih komprehensif yang menggabungkan berbagai algoritma dan domain untuk solusi yang lebih holistik.
