# Implementasi Model Transfer Learning Arsitektur ConvNeXt untuk Klasifikasi Suara Burung di Taman Nasional Way Kambas-Kelompok 13

![image](https://github.com/user-attachments/assets/546cf905-33dd-4c77-a772-7a87ac493110)

Avcla: https://avcla2024.streamlit.app/

anda bisa mencoba test Avcla kami bangun, dengan beberapa audio yang tersedia pada link berikut: https://drive.google.com/drive/folders/1oEdNhsFCuxaBT8VN8tfUHUu-1DX8oNQE?usp=sharing

Kelompok 13 Deep Learning:

- Rizki Adrian Bennovry - 121450073 
  
- Alber Analafean - 121450146 
  
- Nabilah Andika Fitriani - 121450139 

- Catherine Firdhasari Maulina Sinaga - 121450072
  
- Helma Lia Putri - 121450100

Latar Belakang: ....

Tujuan: ......

🎙 Data: 
- https://xeno-canto.org/ (Sumber Data Audio)
- https://avibase.bsc-eoc.org/ (Referensi daftar persebaran burung di area atau kawasan tertentu seluruh dunia)
- https://www.iucnredlist.org/ (Daftar Status Konservasi Hewan)

📊 Metode Pengumpulan Data: Data Crawling (APIs)

📊 Metode Model : Transfer Learning (Arsitektur ConvNeXt type Base)

📊 Model : [https://raw.githubusercontent.com/alberanalafean22/convnextkeras/main/convnextaugmentasiepochs50.keras](https://github.com/alberanalafean22/convnextkeras)

🖥 Bahasa pemrograman: Python, Html, CSS, other

🌐 Hosting dan Development (Streamlit): 

Tahapan Proses:
- Data Crawling
- Data Preprocessing & Processing
- Split Data
- Setting Hyperparamater
- Model Build
- Evaluation Model
- System integration & deployment to website


Hasil Akurasi Implementasi Model dengan beberapa parameter:

| Batch Size | Learning Rate  | Epochs                  | Akurasi |
|------------|----------------|-------------------------|---------|
| 32         |     1e-4       | 25 (Non Augmentasi Data |   0.70  |
| 32         |     1e-4       | 25 (Augmentasi Data)    |   0.65  |
| 32         |     1e-4       |50 (Non Augmentasi Data) |   0.69  |
| 32         |     1e-4       |50 (Augmentasi Data)     |   0.71  |

© Developer: Kelompok 13 Deep Learning
