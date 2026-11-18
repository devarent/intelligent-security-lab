# SUMBER DATASET KEAMANAN SIBER LENGKAP

## 1. KAGGLE

Kaggle menyediakan berbagai dataset keamanan siber yang dapat digunakan untuk penelitian machine learning.

### 1.1 Dataset Populer di Kaggle

#### **UNSW-NB15 Dataset**
- **Link**: https://www.kaggle.com/datasets/mrwells/cyber-security-unsw-nb15
- **Deskripsi**: Dataset intrusion detection yang komprehensif dengan 45 fitur dan 10 kelas serangan
- **Ukuran**: ~2 GB
- **Fitur**: 45 fitur termasuk flow, packet, dan protocol information
- **Kelas**: Normal, Analysis, Backdoor, DoS, Exploits, Fuzzers, Generic, Reconnaissance, Shellcode, Worms
- **Penggunaan**: Cocok untuk deteksi intrusi jaringan

#### **NSL-KDD Dataset**
- **Link**: https://www.kaggle.com/datasets/hassan06/nslkdd
- **Deskripsi**: Dataset klasik untuk intrusion detection
- **Ukuran**: ~150 MB
- **Fitur**: 41 fitur (tidak termasuk label)
- **Kelas**: Normal, DoS, Probe, R2L, U2R
- **Penggunaan**: Baseline untuk penelitian intrusion detection

#### **Network Intrusion Detection Dataset**
- **Link**: https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection
- **Deskripsi**: Dataset untuk deteksi intrusi jaringan
- **Ukuran**: Bervariasi
- **Penggunaan**: Deteksi anomali jaringan

#### **Phishing Dataset**
- **Link**: https://www.kaggle.com/datasets/amanathor/creating-phishing-dataset
- **Deskripsi**: Dataset untuk deteksi phishing
- **Ukuran**: ~500 MB
- **Fitur**: URL features, HTML features
- **Kelas**: Phishing, Legitimate
- **Penggunaan**: Deteksi phishing email dan website

#### **Malware Analysis Dataset**
- **Link**: https://www.kaggle.com/datasets/amauricio/pe-files-malware-analysis
- **Deskripsi**: Dataset PE files untuk analisis malware
- **Ukuran**: ~1 GB
- **Fitur**: PE header features, strings
- **Kelas**: Malware, Benign
- **Penggunaan**: Klasifikasi malware

#### **Botnet Detection Dataset**
- **Link**: https://www.kaggle.com/datasets/mrwells/cic-ids2017
- **Deskripsi**: Dataset untuk deteksi botnet
- **Ukuran**: ~1 GB
- **Penggunaan**: Deteksi botnet traffic

#### **Android Malware Dataset**
- **Link**: https://www.kaggle.com/datasets/xwolf/android-malware-dataset
- **Deskripsi**: Dataset malware Android
- **Ukuran**: ~500 MB
- **Fitur**: APK features, permissions
- **Kelas**: Malware, Benign
- **Penggunaan**: Deteksi malware Android

#### **DDoS Attack Dataset**
- **Link**: https://www.kaggle.com/datasets/goyalshalini93/ddos-attack-dataset
- **Deskripsi**: Dataset untuk deteksi DDoS
- **Ukuran**: ~800 MB
- **Penggunaan**: Deteksi DDoS attacks

#### **CIC-IDS2017 (Kaggle Mirror)**
- **Link**: https://www.kaggle.com/datasets/cicdataset/cicids2017
- **Deskripsi**: Mirror dari CIC-IDS2017 di Kaggle
- **Ukuran**: ~80 GB
- **Penggunaan**: Deteksi intrusi jaringan komprehensif

#### **IoT Malware Dataset**
- **Link**: https://www.kaggle.com/datasets/subhajournal/iot-malware
- **Deskripsi**: Dataset malware untuk IoT
- **Ukuran**: ~2 GB
- **Penggunaan**: Deteksi malware IoT

### 1.2 Cara Download dari Kaggle

```python
# Menggunakan Kaggle API
# Install: pip install kaggle

# 1. Download API key dari Kaggle (Account > Settings > API)
# 2. Letakkan kaggle.json di ~/.kaggle/ (Linux/Mac) atau C:\Users\username\.kaggle\ (Windows)

# Download dataset
import kaggle

# Download UNSW-NB15
kaggle.api.dataset_download_files('mrwells/cyber-security-unsw-nb15', path='data/raw', unzip=True)

# Download NSL-KDD
kaggle.api.dataset_download_files('hassan06/nslkdd', path='data/raw', unzip=True)
```

Atau download secara manual dari website Kaggle.

---

## 2. HUGGING FACE

Hugging Face menyediakan berbagai dataset untuk NLP dan machine learning, termasuk untuk keamanan siber.

### 2.1 Dataset Keamanan Siber di Hugging Face

#### **CyberLLMInstruct**
- **Link**: https://huggingface.co/datasets/cyberllm-instruct/CyberLLMInstruct
- **Deskripsi**: 54,928 instruction-response pairs untuk tugas keamanan siber
- **Format**: JSON
- **Tugas**: Malware analysis, phishing detection, threat intelligence
- **Penggunaan**: Fine-tuning LLM untuk keamanan siber

#### **CTI-HAL (Cyber Threat Intelligence - Human Annotated Labels)**
- **Link**: https://huggingface.co/datasets/cti-hal/CTI-HAL-2025
- **Deskripsi**: Dataset anotasi manusia untuk analisis cyber threat intelligence
- **Format**: JSON
- **Framework**: Mengikuti MITRE ATT&CK
- **Penggunaan**: Optimasi LLM untuk intelijen ancaman

#### **Security Q&A Dataset**
- **Link**: https://huggingface.co/datasets/aliasgharjadi/security-qa
- **Deskripsi**: Dataset Q&A untuk keamanan siber
- **Format**: JSON
- **Penggunaan**: Training chatbot keamanan siber

#### **Cybersecurity Threat Descriptions**
- **Link**: https://huggingface.co/datasets/cyberthreat-descriptions
- **Deskripsi**: Deskripsi ancaman keamanan siber
- **Format**: Text
- **Penggunaan**: NLP untuk keamanan siber

#### **Phishing Email Dataset**
- **Link**: https://huggingface.co/datasets/phishing-emails
- **Deskripsi**: Dataset email phishing dan legitimate
- **Format**: Text/JSON
- **Penggunaan**: Deteksi phishing email

#### **Malware Text Descriptions**
- **Link**: https://huggingface.co/datasets/malware-text
- **Deskripsi**: Deskripsi teks malware
- **Format**: Text
- **Penggunaan**: NLP untuk analisis malware

### 2.2 Cara Download dari Hugging Face

```python
# Install: pip install datasets

from datasets import load_dataset

# Download CyberLLMInstruct
dataset = load_dataset("cyberllm-instruct/CyberLLMInstruct")
print(dataset)

# Download CTI-HAL
dataset = load_dataset("cti-hal/CTI-HAL-2025")
print(dataset)

# Download ke local
dataset.save_to_disk('data/raw/cyberllm_instruct')
```

---

## 3. ULTRALYTICS / YOLO

Ultralytics dan YOLO (You Only Look Once) lebih fokus pada computer vision dan object detection, namun dapat diadaptasi untuk keamanan siber.

### 3.1 YOLO untuk Keamanan Siber

YOLO dapat digunakan untuk:
- **Klasifikasi citra malware** (malware visualization)
- **Deteksi anomali dalam citra**
- **Face recognition untuk biometric security**
- **License plate detection untuk security**

### 3.2 Dataset Kompatibel dengan YOLO

#### **MalNet-Image**
- **Link**: https://malnet.org/
- **Deskripsi**: 1.2+ juta gambar malware
- **Format**: Citra
- **Penggunaan**: Dapat digunakan dengan YOLO untuk klasifikasi malware

#### **CIFAR-10 (Security Context)**
- **Link**: https://www.cs.toronto.edu/~kriz/cifar.html
- **Deskripsi**: Dataset citra standar
- **Penggunaan**: Baseline untuk testing YOLO

#### **ImageNet**
- **Link**: https://www.image-net.org/
- **Deskripsi**: Dataset citra besar
- **Penggunaan**: Pre-training YOLO untuk security applications

### 3.3 Cara Menggunakan YOLO untuk Keamanan Siber

```python
# Install: pip install ultralytics

from ultralytics import YOLO

# Load model
model = YOLO('yolov8n.pt')  # YOLOv8 nano

# Train untuk klasifikasi malware
model.train(
    data='data/malnet.yaml',  # Configuration file
    epochs=50,
    imgsz=64,
    batch=32
)

# Inference
results = model('path/to/malware_image.jpg')
```

**Catatan**: YOLO lebih cocok untuk object detection. Untuk klasifikasi malware, disarankan menggunakan CNN standar seperti yang diimplementasikan di skripsi ini.

---

## 4. SUMBER DATASET LAINNYA

### 4.1 GitHub Repositories

#### **Awesome-Cybersecurity-Datasets**
- **Link**: https://github.com/jasonxp2009/awesome-cybersecurity-datasets
- **Deskripsi**: Kumpulan link dataset keamanan siber
- **Kategori**: Malware, Phishing, Host, Email, Domain, Honeypots
- **Penggunaan**: Referensi sumber dataset

#### **Real-CyberSecurity-Datasets**
- **Link**: https://github.com/andrewaustin/Distributed-Intrusion-Detection-System/tree/master/datasets
- **Deskripsi**: Dataset real-world untuk intrusion detection
- **Penggunaan**: Deteksi intrusi

#### **Malware-Traffic-Analysis.net**
- **Link**: https://www.malware-traffic-analysis.net/
- **Deskripsi**: PCAP files dari malware traffic
- **Format**: PCAP
- **Penggunaan**: Analisis traffic malware

### 4.2 Shadowserver Foundation

- **Link**: https://www.shadowserver.org/
- **Deskripsi**: Lembaga nirlaba yang melakukan pemindaian internet global
- **Data**: Aktivitas botnet, malware, spam
- **Akses**: Gratis untuk pemangku kepentingan
- **Penggunaan**: Intelijen ancaman real-time

### 4.3 MITRE ATT&CK

- **Link**: https://attack.mitre.org/
- **Deskripsi**: Framework knowledge base untuk adversarial tactics
- **Data**: TTPs (Tactics, Techniques, Procedures)
- **Penggunaan**: Reference untuk threat intelligence

### 4.4 CVE (Common Vulnerabilities and Exposures)

- **Link**: https://cve.mitre.org/
- **Deskripsi**: Database kerentanan keamanan
- **Data**: CVE entries
- **Penggunaan**: Analisis kerentanan

### 4.5 CWE (Common Weakness Enumeration)

- **Link**: https://cwe.mitre.org/
- **Deskripsi**: Taksonomi kelemahan perangkat lunak
- **Data**: CWE entries
- **Penggunaan**: Analisis kelemahan

### 4.6 CAPEC (Common Attack Pattern Enumeration and Classification)

- **Link**: https://capec.mitre.org/
- **Deskripsi**: Katalog pola serangan umum
- **Data**: CAPEC entries
- **Penggunaan**: Analisis pola serangan

### 4.7 EUVD (European Union Vulnerability Database)

- **Link**: https://euvd.ec.europa.eu/
- **Deskripsi**: Database kerentanan keamanan Uni Eropa
- **Luncur**: Juni 2024
- **Aktif**: Mei 2025
- **Penggunaan**: Integrasi data kerentanan terbaru

### 4.8 VirusTotal

- **Link**: https://www.virustotal.com/
- **Deskripsi**: Layanan analisis file dan URL
- **API**: VirusTotal API (gratis untuk penggunaan terbatas)
- **Data**: Sample malware, phishing URLs
- **Penggunaan**: Enrichment data dan label

```python
# Contoh menggunakan VirusTotal API
import requests

API_KEY = 'your-api-key'
url = 'https://www.virustotal.com/api/v3/files/{id}'
headers = {'x-apikey': API_KEY}

response = requests.get(url, headers=headers)
data = response.json()
```

### 4.9 AlienVault OTX

- **Link**: https://otx.alienvault.com/
- **Deskripsi**: Open Threat Exchange platform
- **Data**: Indicators of Compromise (IoCs)
- **Akses**: Gratis dengan API
- **Penggunaan**: Threat intelligence

### 4.10 Cuckoo Sandbox

- **Link**: https://cuckoosandbox.org/
- **Deskripsi**: Automated malware analysis system
- **Data**: Malware behavior reports
- **Penggunaan**: Analisis behavior malware

---

## 5. REKOMENDASI PENGGUNAAN DATASET

### 5.1 Untuk Skripsi Ini

**Dataset Utama yang Digunakan:**
1. **CIC-IDS2017/2018** - Dari Canadian Institute for Cybersecurity (sudah dijelaskan di Bab 2)
2. **CIC-DDoS2019** - Dari Canadian Institute for Cybersecurity
3. **CIC-BCCC-NRC TabularIoTAttack-2024** - Dari Canadian Institute for Cybersecurity
4. **MalNet-Image** - Dari MalNet repository
5. **CyberLLMInstruct** - Dari Hugging Face

**Dataset Tambahan yang Dapat Digunakan:**
1. **UNSW-NB15** - Dari Kaggle (sebagai tambahan atau alternatif CIC-IDS)
2. **NSL-KDD** - Dari Kaggle (untuk baseline comparison)
3. **Phishing Dataset** - Dari Kaggle (untuk analisis phishing)

### 5.2 Mapping Dataset ke Model

| Model | Dataset | Sumber |
|-------|---------|--------|
| Isolation Forest | CIC-IDS2017/2018, UNSW-NB15 | CIC / Kaggle |
| Ensemble | CIC-IDS2017/2018, NSL-KDD | CIC / Kaggle |
| CNN | MalNet-Image | MalNet |
| GCN | CIC-BCCC-NRC TabularIoTAttack-2024 | CIC |
| LLM | CyberLLMInstruct, CTI-HAL | Hugging Face |

### 5.3 Cara Menggabungkan Dataset dari Berbagai Sumber

```python
import pandas as pd
from datasets import load_dataset
import kaggle

# 1. Load dari Kaggle
kaggle.api.dataset_download_files('mrwells/cyber-security-unsw-nb15', path='data/raw', unzip=True)
df_kaggle = pd.read_csv('data/raw/UNSW-NB15.csv')

# 2. Load dari Hugging Face
dataset_hf = load_dataset("cyberllm-instruct/CyberLLMInstruct")
df_hf = dataset_hf['train'].to_pandas()

# 3. Load dari local CIC dataset
df_cic = pd.read_csv('data/raw/CIC-IDS2017.csv')

# 4. Preprocessing dan kombinasi
# (sesuai kebutuhan penelitian)
```

---

## 6. PYTHON SCRIPT UNTUK DOWNLOAD DATASET

```python
"""
Script untuk download dataset dari berbagai sumber
"""

import os
import kaggle
from datasets import load_dataset
import pandas as pd
import requests

def download_kaggle_dataset(dataset_name, save_path):
    """Download dataset dari Kaggle"""
    print(f"Downloading {dataset_name} from Kaggle...")
    kaggle.api.dataset_download_files(dataset_name, path=save_path, unzip=True)
    print(f"Downloaded to {save_path}")

def download_huggingface_dataset(dataset_name, save_path):
    """Download dataset dari Hugging Face"""
    print(f"Downloading {dataset_name} from Hugging Face...")
    dataset = load_dataset(dataset_name)
    dataset.save_to_disk(save_path)
    print(f"Downloaded to {save_path}")

def download_from_url(url, save_path):
    """Download dari URL langsung"""
    print(f"Downloading from {url}...")
    response = requests.get(url, stream=True)
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded to {save_path}")

if __name__ == "__main__":
    # Buat direktori
    os.makedirs('data/raw', exist_ok=True)

    # Download dari Kaggle
    download_kaggle_dataset('mrwells/cyber-security-unsw-nb15', 'data/raw/kaggle')
    download_kaggle_dataset('hassan06/nslkdd', 'data/raw/kaggle')

    # Download dari Hugging Face
    download_huggingface_dataset('cyberllm-instruct/CyberLLMInstruct', 'data/raw/huggingface/cyberllm')

    print("All datasets downloaded successfully!")
```

---

## 7. KESIMPULAN

Berbagai sumber dataset tersedia untuk penelitian keamanan siber:

1. **Kaggle**: Banyak dataset populer seperti UNSW-NB15, NSL-KDD, dan mirror dari CIC datasets
2. **Hugging Face**: Dataset NLP seperti CyberLLMInstruct dan CTI-HAL untuk LLM fine-tuning
3. **Ultralytics/YOLO**: Lebih cocok untuk computer vision, dapat diadaptasi untuk malware image classification
4. **GitHub Repositories**: Kumpulan dataset dan resources
5. **Shadowserver**: Data real-time tentang botnet dan malware
6. **MITRE ATT&CK, CVE, CWE**: Knowledge base untuk threat intelligence
7. **VirusTotal, AlienVault OTX**: API untuk enrichment data

Untuk skripsi ini, dataset utama yang digunakan sudah cukup komprehensif (CIC datasets, MalNet-Image, CyberLLMInstruct). Dataset tambahan dari Kaggle dan Hugging Face dapat digunakan sebagai tambahan atau alternatif sesuai kebutuhan penelitian.
