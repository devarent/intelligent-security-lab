# BAB I
# PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi dan komunikasi yang sangat pesat dalam beberapa dekade terakhir telah membawa transformasi fundamental dalam cara manusia berinteraksi, bekerja, dan menjalankan kehidupan sehari-hari. Digitalisasi hampir seluruh aspek kehidupan, mulai dari sistem perbankan, infrastruktur kesehatan, pemerintahan, hingga perangkat rumah tangga yang terhubung ke internet, telah menciptakan ekosistem digital yang sangat kompleks dan saling terkait. Internet of Things (IoT) dan cloud computing telah memperluas permukaan serangan keamanan siber secara eksponensial.

Di sisi lain, ancaman keamanan siber juga berkembang dengan cepat dan menjadi semakin canggih. Laporan dari berbagai lembaga keamanan siber global menunjukkan peningkatan yang signifikan dalam jumlah dan kompleksitas serangan siber setiap tahunnya. Serangan Distributed Denial of Service (DDoS), malware, ransomware, phishing, dan berbagai bentuk intrusi jaringan tidak hanya mengakibatkan kerugian finansial yang besar, tetapi juga mengancam keamanan nasional dan privasi individu.

Metode konvensional untuk deteksi ancaman keamanan siber yang berbasis signature-based (tanda tangan serangan) memiliki keterbatasan yang semakin terlihat. Pendekatan ini hanya mampu mendeteksi serangan yang telah dikenali sebelumnya dan seringkali gagal mengenali serangan baru atau varian yang dimodifikasi. Selain itu, volume data yang sangat besar dari aktivitas jaringan, log sistem, dan aktivitas endpoint membuat analisis manual menjadi tidak praktis dan tidak efisien.

Machine learning sebagai cabang dari kecerdasan buatan (artificial intelligence) menawarkan pendekatan baru yang menjanjikan untuk mengatasi tantangan ini. Algoritma machine learning mampu belajar dari data historis untuk mengenali pola aktivitas normal dan abnormal, sehingga dapat mendeteksi anomali yang mengindikasikan serangan siber secara lebih akurat dan adaptif. Berbagai penelitian telah menunjukkan potensi besar machine learning dalam meningkatkan kinerja sistem deteksi intrusi, klasifikasi malware, dan analisis ancaman siber lainnya.

Canadian Institute for Cybersecurity (CIC) dan berbagai lembaga penelitian lainnya telah menyediakan dataset keamanan siber yang komprehensif dan terstruktur, seperti CIC-IDS2017, CIC-IDS2018, CIC-DDoS2019, dan CIC-BCCC-NRC TabularIoTAttack-2024. Dataset ini mencakup berbagai skenario serangan realistis dan telah menjadi standar dalam penelitian keamanan siber berbasis machine learning. Selain itu, munculnya dataset baru seperti MalNet-Image untuk klasifikasi malware berbasis citra dan CyberLLMInstruct untuk pelatihan Large Language Models (LLM) dalam konteks keamanan siber membuka peluang baru untuk penelitian yang lebih inovatif.

Berdasarkan latar belakang tersebut, penelitian ini berfokus pada implementasi dan analisis komparatif berbagai algoritma machine learning untuk deteksi ancaman keamanan siber yang mencakup berbagai domain: deteksi intrusi jaringan, klasifikasi malware, dan keamanan perangkat IoT. Penelitian ini juga bertujuan untuk mengembangkan dashboard visual berbasis web untuk pemantauan real-time ancaman keamanan siber, sehingga memberikan solusi yang komprehensif dan praktis untuk kebutuhan keamanan siber modern.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah dalam penelitian ini adalah:

1. Bagaimana cara mengimplementasikan preprocessing data untuk dataset keamanan siber yang mencakup normalisasi, pembersihan data, feature engineering, dan penanganan class imbalance?

2. Bagaimana kinerja algoritma Isolation Forest dalam mendeteksi anomali pada lalu lintas jaringan untuk deteksi intrusi?

3. Bagaimana kinerja Convolutional Neural Networks (CNN) dalam klasifikasi malware berbasis citra menggunakan dataset MalNet-Image?

4. Bagaimana kinerja Graph Convolutional Networks (GCN) dalam analisis relasional malware menggunakan dataset graph-based?

5. Bagaimana kinerja metode ensemble dalam menggabungkan prediksi dari berbagai model untuk meningkatkan akurasi deteksi ancaman?

6. Bagaimana kinerja Large Language Models (LLM) yang di-fine-tune menggunakan CyberLLMInstruct untuk analisis intelijen ancaman?

7. Bagaimana komparasi kinerja berbagai algoritma machine learning yang diimplementasikan dalam hal akurasi, precision, recall, F1-score, dan ROC-AUC?

8. Bagaimana mengimplementasikan dashboard web untuk visualisasi dan pemantauan real-time ancaman keamanan siber?

## 1.3 Tujuan Penelitian

Tujuan dari penelitian ini adalah:

1. Mengimplementasikan preprocessing data yang efektif untuk dataset keamanan siber dari berbagai sumber (CIC-IDS2017, CIC-IDS2018, CIC-DDoS2019, CIC-BCCC-NRC TabularIoTAttack-2024, MalNet-Image, dan CyberLLMInstruct).

2. Mengimplementasikan dan mengevaluasi kinerja algoritma Isolation Forest untuk deteksi anomali pada lalu lintas jaringan.

3. Mengimplementasikan dan mengevaluasi kinerja Convolutional Neural Networks (CNN) untuk klasifikasi malware berbasis citra.

4. Mengimplementasikan dan mengevaluasi kinerja Graph Convolutional Networks (GCN) untuk analisis relasional malware.

5. Mengimplementasikan dan mengevaluasi kinerja metode ensemble untuk meningkatkan akurasi deteksi ancaman.

6. Mengimplementasikan dan mengevaluasi kinerja Large Language Models (LLM) yang di-fine-tune untuk analisis intelijen ancaman.

7. Melakukan analisis komparatif kinerja berbagai algoritma machine learning yang diimplementasikan menggunakan metrik evaluasi yang sesuai.

8. Mengembangkan dashboard web untuk visualisasi dan pemantauan real-time ancaman keamanan siber.

## 1.4 Manfaat Penelitian

Penelitian ini diharapkan memberikan manfaat bagi berbagai pihak:

### 1.4.1 Manfaat Akademis
1. Menambah kontribusi ilmiah dalam bidang keamanan siber dan machine learning, khususnya dalam hal implementasi berbagai algoritma untuk deteksi ancaman keamanan siber.
2. Menyediakan referensi dan dasar bagi penelitian selanjutnya yang terkait dengan penerapan machine learning dalam keamanan siber.
3. Memberikan pemahaman yang lebih komprehensif tentang kelebihan dan keterbatasan berbagai algoritma machine learning dalam konteks keamanan siber.

### 1.4.2 Manfaat Praktis
1. Memberikan solusi deteksi ancaman keamanan siber yang lebih akurat dan adaptif bagi organisasi dan institusi yang membutuhkan sistem keamanan yang efektif.
2. Dashboard web yang dikembangkan dapat digunakan sebagai alat pemantauan real-time ancaman keamanan siber.
3. Implementasi kode program yang disediakan dapat diadaptasi dan dikembangkan lebih lanjut sesuai kebutuhan spesifik organisasi.

### 1.4.3 Manfaat bagi Penulis
1. Mengembangkan kemampuan teknis dalam implementasi machine learning untuk keamanan siber.
2. Memperdalam pemahaman tentang berbagai algoritma machine learning dan penerapannya dalam konteks nyata.
3. Meningkatkan kemampuan dalam pengolahan data, analisis, dan pengembangan sistem visualisasi.

## 1.5 Batasan Masalah

Agar penelitian ini dapat terarah dan terukur, maka dibuat batasan masalah sebagai berikut:

1. Dataset yang digunakan terbatas pada dataset publik yang tersedia: CIC-IDS2017, CIC-IDS2018, CIC-DDoS2019, CIC-BCCC-NRC TabularIoTAttack-2024, MalNet-Image, dan CyberLLMInstruct. Tidak menggunakan data proprietary dari organisasi tertentu.

2. Algoritma machine learning yang diimplementasikan terbatas pada: Isolation Forest, Convolutional Neural Networks (CNN), Graph Convolutional Networks (GCN), metode ensemble (Random Forest, XGBoost, Voting Classifier), dan fine-tuning LLM dengan CyberLLMInstruct.

3. Fokus penelitian adalah pada deteksi ancaman keamanan siber di tiga domain utama: jaringan (network intrusion), malware, dan perangkat IoT. Tidak mencakup semua jenis ancaman keamanan siber yang ada.

4. Evaluasi model dilakukan menggunakan metrik standar: akurasi, precision, recall, F1-score, dan ROC-AUC. Tidak melakukan analisis performa komputasi secara mendalam.

5. Dashboard web yang dikembangkan berfokus pada visualisasi dan pemantauan ancaman keamanan siber berbasis data yang telah diproses. Tidak mencakup integrasi dengan sistem monitoring real-time yang terhubung langsung ke jaringan atau infrastruktur produksi.

6. Implementasi LLM terbatas pada fine-tuning model yang ada menggunakan dataset CyberLLMInstruct untuk tugas analisis intelijen ancaman. Tidak melatih model LLM dari awal (pre-training).

7. Penelitian ini menggunakan bahasa pemrograman Python dengan framework machine learning seperti TensorFlow/Keras, PyTorch, Scikit-learn, dan library pendukung lainnya.

## 1.6 Sistematika Penulisan

Sistematika penulisan skripsi ini disusun sebagai berikut:

**BAB I PENDAHULUAN**
Bab ini menjelaskan latar belakang penelitian, rumusan masalah, tujuan penelitian, manfaat penelitian, batasan masalah, dan sistematika penulisan.

**BAB II TINJAUAN PUSTAKA**
Bab ini membahas teori dan konsep yang menjadi dasar penelitian, meliputi keamanan siber, machine learning, algoritma-algoritma yang digunakan, dataset keamanan siber, preprocessing data, dan penelitian terdahulu yang relevan.

**BAB III METODOLOGI PENELITIAN**
Bab ini menjelaskan tahapan penelitian, pengumpulan data, preprocessing data, perancangan model machine learning, pelatihan dan evaluasi model, metrik evaluasi, pengembangan dashboard web, dan alur penelitian secara keseluruhan.

**BAB IV IMPLEMENTASI**
Bab ini menjelaskan lingkungan pengembangan, implementasi preprocessing data, implementasi setiap model machine learning, implementasi dashboard web, dan dokumentasi kode program.

**BAB V HASIL DAN PEMBAHASAN**
Bab ini menyajikan hasil dari implementasi, mencakup hasil preprocessing data, hasil pelatihan setiap model, analisis komparatif kinerja model, analisis sensitivitas parameter, hasil implementasi dashboard web, dan pembahasan mendalam terhadap hasil yang diperoleh.

**BAB VI KESIMPULAN DAN SARAN**
Bab ini menyajikan kesimpulan dari seluruh penelitian yang telah dilakukan, serta memberikan saran untuk pengembangan dan penelitian selanjutnya.

**DAFTAR PUSTAKA**
Berisi daftar referensi yang digunakan dalam penulisan skripsi ini.

**LAMPIRAN**
Berisi kode program lengkap, deskripsi dataset, hasil evaluasi yang lebih detail, dan manual penggunaan dashboard.
