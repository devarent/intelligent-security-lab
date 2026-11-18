# BAB VI
# KESIMPULAN DAN SARAN

## 6.1 Kesimpulan

Berdasarkan hasil penelitian yang telah dilakukan mengenai implementasi machine learning untuk deteksi ancaman keamanan siber dengan studi komparatif berbagai algoritma pada jaringan, malware, dan perangkat IoT, maka dapat ditarik kesimpulan sebagai berikut:

### 6.1.1 Implementasi Preprocessing Data

1. Preprocessing data yang mencakup data cleaning, normalisasi, feature engineering, encoding data kategorikal, dan handling class imbalance terbukti sangat penting dan memberikan dampak signifikan terhadap kinerja model machine learning.

2. Normalisasi data menggunakan StandardScaler dan MinMaxScaler meningkatkan akurasi ensemble model sebesar 3.69% (dari 93.2% menjadi 96.89%), karena memastikan semua fitur memiliki skala yang seragam sehingga model tidak bias ke fitur dengan skala besar.

3. Feature engineering yang menambahkan time-based features, ratio features, dan statistical features meningkatkan akurasi sebesar 1.5-2.0%, karena memberikan informasi yang lebih kaya dan relevan untuk deteksi ancaman.

4. Penerapan SMOTE untuk handling class imbalance meningkatkan recall sebesar 7.95% (dari 88.5% menjadi 96.45%), karena menyeimbangkan distribusi kelas sehingga model tidak bias ke kelas mayoritas (normal).

5. Proses preprocessing berhasil menghapus missing values, duplikasi, dan outliers, serta mengubah data kategorikal menjadi format numerik yang dapat diproses oleh model machine learning.

### 6.1.2 Kinerja Algoritma Isolation Forest

1. Isolation Forest mencapai akurasi 89.45% pada dataset CIC-IDS2017 dan 91.23% pada dataset CIC-IDS2018, menunjukkan kinerja yang baik untuk deteksi anomali secara unsupervised.

2. Recall yang tinggi (91.34% pada CIC-IDS2017 dan 93.12% pada CIC-IDS2018) menunjukkan bahwa Isolation Forest efektif dalam mendeteksi sebagian besar serangan, namun false positive rate yang relatif tinggi (11.33% dan 9.55%) masih menjadi tantangan.

3. Training time yang sangat cepat (45.2 detik untuk CIC-IDS2017 dan 247.8 detik untuk CIC-IDS2018) dan inference time yang sangat rendah (0.002 detik per sample) membuat Isolation Forest sangat cocok untuk real-time anomaly detection sebagai pre-filter.

4. Parameter n_estimators=100 dan contamination=0.05 memberikan balance terbaik antara akurasi dan computational cost.

### 6.1.3 Kinerja Convolutional Neural Networks (CNN)

1. CNN mencapai akurasi 92.45% pada dataset MalNet-Image untuk klasifikasi malware berbasis citra, menunjukkan efektivitas tinggi tanpa memerlukan feature engineering konvensional.

2. Arsitektur CNN dengan 3 convolutional blocks, batch normalization, dan dropout mencapai kinerja yang baik dengan training time 54 menit dan inference time 0.015 detik per image.

3. Ransomware memiliki kinerja terbaik (F1-Score 94.39%), sedangkan Adware memiliki kinerja terendah (F1-Score 88.27%), menunjukkan bahwa beberapa jenis malware memiliki pattern visual yang lebih distinct daripada yang lain.

4. Data augmentation dengan rotation, shift, flip, dan zoom membantu mencegah overfitting dan meningkatkan generalisasi model.

### 6.1.4 Kinerja Graph Convolutional Networks (GCN)

1. GCN mencapai akurasi 85.23% pada dataset graph-based untuk analisis relasional malware, menunjukkan kemampuan yang baik dalam menangkap pola relasional antar entitas.

2. GCN sangat berguna untuk analisis forensik di mana memahami relasi antar file, proses, dan entitas sistem penting untuk memahami chain of attack.

3. Training time 31 menit dan inference time 0.008 detik per graph membuat GCN cukup efisien untuk analisis graph yang kompleks.

4. Kinerja GCN sedikit lebih rendah dibandingkan CNN (85.23% vs 92.45%), namun menawarkan interpretasi yang lebih baik terkait relasi antar entitas.

### 6.1.5 Kinerja Ensemble Methods

1. Ensemble model dengan stacking (Random Forest + XGBoost + LightGBM sebagai base models dan Logistic Regression sebagai meta-model) mencapai kinerja terbaik dibandingkan semua model individual lainnya.

2. Ensemble model mencapai akurasi 96.89% pada CIC-IDS2017 dan 97.34% pada CIC-IDS2018, dengan F1-Score 96.28% dan 97.00%, serta ROC-AUC 0.9876 dan 0.9912.

3. False positive rate yang sangat rendah (sekitar 4.7%) membuat ensemble model sangat cocok untuk production system untuk mengurangi alert fatigue di SOC.

4. Training time yang lebih lama (589 detik untuk CIC-IDS2017 dan 3,245 detik untuk CIC-IDS2018) namun masih acceptable mengingat kinerja yang sangat baik.

5. Cross-validation menunjukkan bahwa LightGBM memiliki kinerja terbaik di antara base models (95.67% mean CV accuracy), namun stacking memberikan peningkatan tambahan sebesar 1.22%.

### 6.1.6 Kinerja Large Language Models (LLM)

1. LLM (BERT-base) yang di-fine-tune menggunakan dataset CyberLLMInstruct mencapai BLEU score 0.7234, ROUGE-1 0.8156, dan ROUGE-L 0.7892, menunjukkan kemampuan yang baik dalam menghasilkan response yang relevan untuk tugas keamanan siber.

2. LLM dapat memberikan analisis interpretatif dan rekomendasi yang natural dan actionable, berbeda dengan model klasifikasi yang hanya memberikan label.

3. Training time 3.4 jam dan inference time 0.5 detik per response membuat LLM lebih cocok untuk threat intelligence dan analysis daripada real-time detection.

4. LLM sangat berguna untuk analisis log keamanan siber, pembuatan laporan otomatis, dan memberikan insight yang berharga kepada analis keamanan.

### 6.1.7 Analisis Komparatif

1. Ensemble model mencapai kinerja terbaik secara keseluruhan dengan akurasi di atas 96%, diikuti oleh CNN (92.45%), GCN (85.23%), dan Isolation Forest (89-91%).

2. Trade-off yang perlu dipertimbangkan: model dengan akurasi lebih tinggi (ensemble, CNN) memiliki training time yang lebih lama, sedangkan model dengan training time cepat (Isolation Forest) memiliki akurasi yang sedikit lebih rendah.

3. Setiap algoritma memiliki use case terbaik: Isolation Forest untuk real-time anomaly detection, CNN untuk klasifikasi malware berbasis citra, GCN untuk analisis relasional, ensemble untuk high-accuracy detection, dan LLM untuk threat intelligence.

### 6.1.8 Implementasi Dashboard Web

1. Dashboard web berhasil diimplementasikan dengan fitur real-time monitoring, model performance visualization, threat intelligence, historical analysis, dan export functionality.

2. Dashboard memiliki performance yang baik dengan page load time 1.2 detik, API response time 0.15 detik, dan memory usage yang masih dalam batas reasonable.

3. Dashboard memungkinkan monitoring real-time ancaman keamanan siber dengan visualisasi yang mudah dipahami oleh analis keamanan.

### 6.1.9 Pencapaian Tujuan Penelitian

1. Berhasil mengimplementasikan preprocessing data yang efektif untuk dataset keamanan siber dari berbagai sumber (CIC-IDS2017, CIC-IDS2018, CIC-DDoS2019, CIC-BCCC-NRC TabularIoTAttack-2024, MalNet-Image, dan CyberLLMInstruct).

2. Berhasil mengimplementasikan dan mengevaluasi kinerja algoritma Isolation Forest untuk deteksi anomali pada lalu lintas jaringan dengan akurasi 89-91%.

3. Berhasil mengimplementasikan dan mengevaluasi kinerja Convolutional Neural Networks (CNN) untuk klasifikasi malware berbasis citra dengan akurasi 92.45%.

4. Berhasil mengimplementasikan dan mengevaluasi kinerja Graph Convolutional Networks (GCN) untuk analisis relasional malware dengan akurasi 85.23%.

5. Berhasil mengimplementasikan dan mengevaluasi kinerja metode ensemble untuk meningkatkan akurasi deteksi ancaman hingga 96-97%.

6. Berhasil mengimplementasikan dan mengevaluasi kinerja Large Language Models (LLM) yang di-fine-tune untuk analisis intelijen ancaman dengan BLEU score 0.7234.

7. Berhasil melakukan analisis komparatif kinerja berbagai algoritma machine learning yang diimplementasikan menggunakan metrik evaluasi yang sesuai.

8. Berhasil mengembangkan dashboard web untuk visualisasi dan pemantauan real-time ancaman keamanan siber dengan performance yang baik.

## 6.2 Saran

Berdasarkan hasil penelitian dan kesimpulan yang telah diperoleh, maka beberapa saran yang dapat diajukan untuk pengembangan selanjutnya adalah:

### 6.2.1 Saran untuk Penelitian Lanjutan

1. **Uji Coba pada Data Real-Time**
   Penelitian ini hanya menggunakan dataset publik yang sudah diberi label. Penelitian lanjutan sebaiknya menguji model pada data real-time dari production environment untuk mengevaluasi kinerja dalam kondisi nyata.

2. **Evaluasi terhadap Adversarial Attacks**
   Model belum diuji terhadap adversarial attacks yang dapat memanipulasi input untuk menghindari deteksi. Penelitian lanjutan sebaiknya mengevaluasi robustness model terhadap adversarial examples dan mengembangkan teknik untuk meningkatkan robustness.

3. **Penanganan Concept Drift**
   Pola serangan siber terus berkembang dan berubah seiring waktu. Penelitian lanjutan sebaiknya mengembangkan mekanisme untuk mendeteksi dan menangani concept drift, serta implementasi periodic retraining secara otomatis.

4. **Scalability Evaluation**
   Penelitian lanjutan sebaiknya mengevaluasi kinerja model pada data dengan volume yang sangat besar (petabytes) dan mengembangkan teknik untuk mempercepat training dan inference pada data skala besar.

5. **Federated Learning**
   Mengembangkan sistem berbasis federated learning untuk memungkinkan multiple organisasi berkolaborasi dalam melatih model tanpa membagikan data sensitif, meningkatkan privasi dan security.

6. **Explainable AI (XAI)**
   Mengembangkan teknik explainable AI untuk memberikan interpretasi yang lebih baik tentang mengapa model membuat prediksi tertentu, meningkatkan trust dan interpretability.

7. **Integration dengan MITRE ATT&CK**
   Mengintegrasikan model dengan MITRE ATT&CK framework untuk mapping serangan yang terdeteksi ke teknik dan tactic spesifik, meningkatkan konteks dan actionable intelligence.

8. **AutoML untuk Keamanan Siber**
   Mengembangkan sistem AutoML yang dapat secara otomatis memilih dan mengoptimalkan model terbaik untuk dataset keamanan siber spesifik, mengurangi manual tuning.

### 6.2.2 Saran untuk Implementasi Production

1. **Hybrid Detection System**
   Implementasikan hybrid system yang menggabungkan Isolation Forest untuk real-time filtering, diikuti oleh ensemble model untuk klasifikasi detail, memberikan balance antara kecepatan dan akurasi.

2. **Periodic Retraining**
   Implementasikan periodic retraining (misalnya bulanan atau quarterly) untuk menangani concept drift dan memastikan model tetap relevan dengan pola serangan baru.

3. **Ensemble with Voting**
   Gunakan voting classifier untuk robustness terhadap failure satu model, meningkatkan reliability sistem production.

4. **Human-in-the-Loop**
   Integrasi LLM untuk memberikan interpretasi dan rekomendasi, namun tetap memerlukan review oleh analis keamanan untuk validasi dan quality control.

5. **Resource Optimization**
   Implementasikan model quantization, pruning, dan distillation untuk mengurangi memory footprint dan inference time, memungkinkan deployment pada resource-constrained environments.

6. **Model Versioning and Monitoring**
   Implementasikan sistem model versioning (misalnya menggunakan MLflow) dan monitoring continuous untuk mendeteksi performance degradation dan triggering retraining.

7. **Alert Prioritization**
   Integrasi dengan sistem alert prioritization berdasarkan severity dan confidence score model, membantu analis keamanan fokus pada ancaman yang paling kritis.

8. **Multi-Tenant Architecture**
   Untuk solusi cloud-based, implementasikan multi-tenant architecture dengan proper isolation dan security untuk multiple organisasi.

### 6.2.3 Saran untuk Pengembangan Dashboard

1. **Real-time Alerting**
   Tambahkan fitur real-time alerting dengan notification (email, SMS, Slack) untuk serangan yang terdeteksi dengan confidence score tinggi.

2. **Advanced Visualization**
   Implementasikan advanced visualization seperti network graphs untuk visualisasi relasi antar entitas, heatmaps untuk spatial analysis, dan timeline untuk forensic analysis.

3. **Collaboration Features**
   Tambahkan fitur collaboration seperti annotations, comments, dan case management untuk memungkinkan tim keamanan bekerja sama dalam menangani insiden.

4. **Customizable Dashboards**
   Implementasikan customizable dashboards di mana user dapat membuat dan menyimpan custom views sesuai kebutuhan spesifik mereka.

5. **Mobile Application**
   Kembangkan mobile application untuk memungkinkan monitoring on-the-go dan push notifications untuk critical alerts.

6. **Integration dengan SIEM**
   Integrasi dengan Security Information and Event Management (SIEM) systems seperti Splunk, ELK Stack, atau QRadar untuk unified security monitoring.

7. **API untuk Third-Party Integration**
   Tambahkan comprehensive API documentation untuk memungkinkan third-party integrasi dan automation.

### 6.2.4 Saran untuk Pengembangan Dataset

1. **Dataset dengan Label yang Lebih Detail**
   Pengembangan dataset dengan label yang lebih detail tidak hanya jenis serangan, tetapi juga severity, impact, dan recommended response.

2. **Dataset dengan Ground Truth**
   Dataset dengan ground truth yang valid dan terverifikasi untuk memastikan kualitas label dan mengurangi noise.

3. **Dataset dengan Temporal Information**
   Dataset dengan temporal information yang lebih detail untuk memungkinkan analisis time series dan deteksi pattern temporal.

4. **Dataset Multimodal**
   Pengembangan dataset multimodal yang menggabungkan network traffic, log sistem, endpoint data, dan teks threat intelligence untuk more comprehensive analysis.

5. **Dataset untuk Adversarial Training**
   Dataset yang mencakup adversarial examples untuk melatih model yang lebih robust terhadap adversarial attacks.

6. **Dataset dengan Privacy Preservation**
   Dataset yang telah di-anonymize dan dipreserved privasinya untuk memungkinkan sharing tanpa mengorbankan privasi data sensitif.

### 6.2.5 Saran untuk Akademisi dan Praktisi

1. **Kolaborasi Akademia-Industri**
   Dorong kolaborasi yang lebih erat antara akademia dan industri untuk memastikan penelitian relevan dengan kebutuhan praktis dan industri dapat mengadopsi hasil penelitian.

2. **Open Source Contribution**
   Dorong open source contribution untuk kode program, model, dan dataset untuk mempercepat inovasi dan memungkinkan reproducibility penelitian.

3. **Standardization**
   Dorong standardization dalam metrik evaluasi, dataset, dan benchmark untuk memungkinkan comparison yang fair antar penelitian.

4. **Education and Training**
   Tingkatkan education dan training tentang machine learning untuk keamanan siber di kalangan praktisi dan akademisi untuk meningkatkan adopsi dan kompetensi.

5. **Ethical Considerations**
   Pertimbangkan ethical implications dari penggunaan AI dalam keamanan siber, termasuk bias, privacy, dan potensi misuse.

6. **Regulatory Compliance**
   Pastikan implementasi mematuhi regulatory requirements seperti GDPR, HIPAA, dan regulasi lainnya terkait data privacy dan security.

Penelitian ini diharapkan dapat memberikan kontribusi yang berharga bagi pengembangan sistem deteksi ancaman keamanan siber berbasis machine learning dan menjadi dasar bagi penelitian-penelitian selanjutnya di bidang ini. Dengan terus berkembangnya teknologi AI dan semakin kompleksnya ancaman siber, penelitian di bidang ini akan terus relevan dan penting untuk masa depan keamanan digital.
