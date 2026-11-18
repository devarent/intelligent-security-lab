# SKRIPSI

## IMPLEMENTASI MACHINE LEARNING UNTUK DETEKSI ANCAMAN KEAMANAN SIBER: STUDI KOMPARATIF BERBAGAI ALGORITMA PADA JARINGAN, MALWARE, DAN PERANGKAT IoT

Oleh:
**Muhammad Arya Fatthurahman**
NIM: 2023230006

Program Studi Teknik Informatika
Fakultas Teknik
Universitas [Nama Universitas]

Tahun 2026

---

## ABSTRAK

Perkembangan teknologi informasi yang pesat membawa dampak signifikan terhadap meningkatnya ancaman keamanan siber di berbagai sektor. Serangan siber seperti Distributed Denial of Service (DDoS), malware, dan intrusi jaringan menjadi semakin kompleks dan sulit dideteksi dengan metode konvensional. Penelitian ini bertujuan untuk mengimplementasikan dan menganalisis kinerja berbagai algoritma machine learning untuk deteksi ancaman keamanan siber yang mencakup deteksi intrusi jaringan, klasifikasi malware, dan keamanan perangkat Internet of Things (IoT).

Penelitian ini menggunakan dataset publik terpercaya dari Canadian Institute for Cybersecurity (CIC) yang meliputi CIC-IDS2017, CIC-IDS2018, CIC-DDoS2019, dan CIC-BCCC-NRC TabularIoTAttack-2024. Beberapa algoritma machine learning yang diimplementasikan meliputi Isolation Forest untuk deteksi anomali, Convolutional Neural Networks (CNN) untuk klasifikasi malware berbasis citra, Graph Convolutional Networks (GCN) untuk analisis relasional malware, metode ensemble untuk kombinasi prediksi, serta model LLM yang di-fine-tune menggunakan CyberLLMInstruct untuk analisis intelijen ancaman.

Proses preprocessing data mencakup normalisasi, pembersihan data, feature engineering, encoding data kategorikal, dan penanganan class imbalance menggunakan teknik SMOTE. Evaluasi model dilakukan menggunakan metrik akurasi, precision, recall, F1-score, dan ROC-AUC.

Hasil penelitian menunjukkan bahwa kombinasi metode ensemble dengan preprocessing yang tepat mampu mencapai akurasi deteksi ancaman di atas 95% untuk berbagai jenis serangan. Model CNN berbasis citra malware menunjukkan efektivitas tinggi dalam klasifikasi tanpa memerlukan feature engineering konvensional. Sedangkan model LLM yang di-fine-tune memberikan kemampuan analisis interpretatif yang baik untuk konteks intelijen ancaman. Penelitian ini juga mengembangkan dashboard visual berbasis web untuk pemantauan real-time ancaman keamanan siber.

**Kata Kunci:** Machine Learning, Keamanan Siber, Deteksi Intrusi, Malware, IoT, Isolation Forest, CNN, Ensemble Learning

---

## KATA PENGANTAR

Puji syukur penulis panjatkan ke hadirat Allah SWT yang telah memberikan rahmat dan karunia-Nya sehingga penulis dapat menyelesaikan skripsi ini dengan judul "Implementasi Machine Learning untuk Deteksi Ancaman Keamanan Siber: Studi Komparatif Berbagai Algoritma pada Jaringan, Malware, dan Perangkat IoT".

Penulisan skripsi ini bertujuan untuk memenuhi salah satu syarat dalam menyelesaikan program studi Teknik Informatika di Fakultas Teknik Universitas [Nama Universitas]. Dalam proses penyusunan skripsi ini, penulis mendapatkan banyak bantuan, bimbingan, dan dukungan dari berbagai pihak. Oleh karena itu, pada kesempatan ini penulis menyampaikan terima kasih kepada:

1. Bapak/Ibu Dosen Pembimbing yang telah memberikan bimbingan, arahan, dan masukan yang berharga selama proses penyusunan skripsi ini.
2. Seluruh dosen dan staf program studi Teknik Informatika yang telah memberikan ilmu pengetahuan selama masa perkuliahan.
3. Orang tua dan keluarga yang telah memberikan dukungan moral dan material sehingga penulis dapat menyelesaikan studi ini.
4. Teman-teman dan rekan sejawat yang telah memberikan semangat dan motivasi.

Penulis menyadari bahwa skripsi ini masih jauh dari sempurna. Oleh karena itu, penulis mengharapkan kritik dan saran yang membangun dari pembaca demi perbaikan di masa mendatang. Semoga skripsi ini dapat bermanfaat bagi pembaca dan memberikan kontribusi dalam pengembangan ilmu pengetahuan di bidang keamanan siber.

[Tempat], [Tanggal]

Penulis,

Muhammad Arya Fatthurahman
NIM: 2023230006

---

## DAFTAR ISI

ABSTRAK
KATA PENGANTAR
DAFTAR ISI
DAFTAR TABEL
DAFTAR GAMBAR
DAFTAR NOTASI

BAB I PENDAHULUAN
1.1 Latar Belakang
1.2 Rumusan Masalah
1.3 Tujuan Penelitian
1.4 Manfaat Penelitian
1.5 Batasan Masalah
1.6 Sistematika Penulisan

BAB II TINJAUAN PUSTAKA
2.1 Keamanan Siber
2.1.1 Jenis-Jenis Serangan Siber
2.1.2 Tantangan Deteksi Serangan Siber
2.2 Machine Learning
2.2.1 Supervised Learning
2.2.2 Unsupervised Learning
2.2.3 Deep Learning
2.3 Algoritma Machine Learning untuk Keamanan Siber
2.3.1 Isolation Forest
2.3.2 Convolutional Neural Networks (CNN)
2.3.3 Graph Convolutional Networks (GCN)
2.3.4 Ensemble Methods
2.3.5 Large Language Models (LLM)
2.4 Dataset Keamanan Siber
2.4.1 CIC-IDS2017
2.4.2 CIC-IDS2018
2.4.3 CIC-DDoS2019
2.4.4 CIC-BCCC-NRC TabularIoTAttack-2024
2.4.5 MalNet-Image
2.4.6 CyberLLMInstruct
2.5 Preprocessing Data
2.5.1 Normalisasi dan Standarisasi
2.5.2 Feature Engineering
2.5.3 Handling Class Imbalance
2.5.4 Encoding Data Kategorikal
2.6 Penelitian Terdahulu

BAB III METODOLOGI PENELITIAN
3.1 Tahapan Penelitian
3.2 Pengumpulan Data
3.3 Preprocessing Data
3.4 Perancangan Model Machine Learning
3.4.1 Model Deteksi Anomali dengan Isolation Forest
3.4.2 Model Klasifikasi Malware dengan CNN
3.4.3 Model Analisis Relasional dengan GCN
3.4.4 Model Ensemble
3.4.5 Model LLM untuk Intelijen Ancaman
3.5 Pelatihan dan Evaluasi Model
3.6 Metrik Evaluasi
3.7 Pengembangan Dashboard Web
3.8 Alur Penelitian

BAB IV IMPLEMENTASI
4.1 Lingkungan Pengembangan
4.2 Implementasi Preprocessing Data
4.3 Implementasi Model Isolation Forest
4.4 Implementasi Model CNN
4.5 Implementasi Model GCN
4.6 Implementasi Model Ensemble
4.7 Implementasi Model LLM
4.8 Implementasi Dashboard Web
4.9 Dokumentasi Kode Program

BAB V HASIL DAN PEMBAHASAN
5.1 Hasil Preprocessing Data
5.2 Hasil Pelatihan Model Isolation Forest
5.3 Hasil Pelatihan Model CNN
5.4 Hasil Pelatihan Model GCN
5.5 Hasil Pelatihan Model Ensemble
5.6 Hasil Pelatihan Model LLM
5.7 Analisis Komparatif Kinerja Model
5.8 Analisis Sensitivitas Parameter
5.9 Hasil Implementasi Dashboard Web
5.10 Pembahasan

BAB VI KESIMPULAN DAN SARAN
6.1 Kesimpulan
6.2 Saran

DAFTAR PUSTAKA

LAMPIRAN
Lampiran A: Kode Program Lengkap
Lampiran B: Dataset Deskripsi
Lampiran C: Hasil Evaluasi Lengkap
Lampiran D: Manual Penggunaan Dashboard
