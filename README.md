# **Implementasi Model Transfer Learning Arsitektur ConvNeXt untuk Klasifikasi Suara Burung di Taman Nasional Way Kambas- Kelompok 13 (Avcla)**

![image](https://github.com/user-attachments/assets/546cf905-33dd-4c77-a772-7a87ac493110)

## Kelompok 13 Deep Learning

- Rizki Adrian Bennovry - 121450073 
  
- Alber Analafean - 121450146 
  
- Nabilah Andika Fitriani - 121450139 

- Catherine Firdhasari Maulina Sinaga - 121450072
  
- Helma Lia Putri - 121450100

## 📱**AVCLA, apa itu?** 

**AVCLA (Aves Classification Apps)**, merupakan sebuah website dalam mendeteksi klasifikasi burung di kawasan **Taman Nasional Way Kambas**. Website ini bisa mendeteksi klasifikasi pada 10 spesies burung, dengan **Implementasi metode Deep Learning menggunakan Transfer Learning dengan arsitektur Convnext Type Base**. Website ini bisa memprediksi spesies burung berdasarkan suara yang diberikan. Model yang digunakan pada deployment adalah model yang terbaik dari beberapa parameter yang telah digunakan dalam memperoleh performa dan akurasi sangat baik.

Anda bisa mencoba test pengguna **Avcla** kami kembangkan, dengan beberapa audio yang tersedia pada link berikut: https://drive.google.com/drive/folders/1oEdNhsFCuxaBT8VN8tfUHUu-1DX8oNQE?usp=sharing.

Berikut Link AVCLA : https://avcla2024.streamlit.app/ (Versi Beta)

## 🎙 Data 
- https://xeno-canto.org/ (Sumber Data Audio)
- https://avibase.bsc-eoc.org/ (Referensi daftar persebaran burung di area atau kawasan tertentu seluruh dunia)

## 📂 Metode Pengumpulan Data
Data Crawling (APIs)

## 📊 Metode Deep Learning 
Transfer Learning (Arsitektur ConvNeXt type Base)

## 🧠 Model  

#### [https://raw.githubusercontent.com/alberanalafean22/convnextkeras/main/convnextaugmentasiepochs50.keras](https://github.com/alberanalafean22/convnextkeras)

## 🖥 Bahasa Pemrograman & Library 
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) ![HTML](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white)  ![CSS](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white) ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)  ![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)  ![Keras](https://img.shields.io/badge/-Keras-D00000?style=flat&logo=keras&logoColor=white)  ![Librosa](https://img.shields.io/badge/-Librosa-FF6F00?style=flat&logo=soundcloud&logoColor=white)  ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)  ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat&logo=python&logoColor=white) 

## 🌐 Hosting dan Development
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)


## 📚Tahapan Proses
- Data Crawling
- Data Preprocessing & Processing
- Split Data
- Setting Hyperparamater
- Model Build
- Evaluation Model
- System integration & deployment to website


## 📈 Akurasi Model 

Diperoleh Hasil Akurasi Implementasi Model dengan beberapa parameter:

| Batch Size | Learning Rate  | Epochs                   | Akurasi |
|------------|----------------|--------------------------|---------|
| 32         |     0.0001     | 25 (Non Augmentasi Data  |   0.70  |
| 32         |     0.0001     | 25 (Augmentasi Data)     |   0.65  |
| 32         |     0.0001     | 50 (Non Augmentasi Data) |   0.69  |
| **32**     |   **0.0001**   | **50 (Augmentasi Data)**   | **0.71** |


### 📳 Panduan Penggunaan Avcla:

1. Anda Terlebih dahulu, silahkan buka browser anda pada perangkat anda (smartphone atau pc) dan lalu tulis ataupun klik link berikut : https://avcla2024.streamlit.app/

2. Selanjutnya input audio burung yang untuk mengetahui klasifikasi spesies burung pada bagian browser files (ketentuan audio yang bisa diinput berformat mp3, dengan limit maksimum ukuran file 200 mb.

![image](https://github.com/user-attachments/assets/546cf905-33dd-4c77-a772-7a87ac493110)

3. Setelah audio di input, tunggu beberapa detik, dan diperoleh hasil klasifikasi spesies burungnya dengan nama spesies burungnya, akurasi prediksi-nya bahkan terdapat QR Code untuk mengetahui informasi detail dari burung tersebut.

![image](https://github.com/user-attachments/assets/8500766d-88f1-436e-937c-95b87179e459)

4. Dan anda juga bisa melihat direktori Avcla pada link github ini terkait informasi model ataupun deployment. 

5. Jika anda terdapat Kritik, Saran, kendala terkait teknis penggunaan Avcla bisa menghubungi:
 
#### Email Team - deeplearning13project@gmail.com

#### Developer Avcla - alber.121450146@student.itera.ac.id

Panduan penggunaan Avcla juga bisa diakses pada link berikut : youtube.com/???


### Salam hangat dari kami Kelompok 13 Deep Learning TA 2024/2025
### © Developer: Kelompok 13 Deep Learning
### #FromSumateraForSumatera #DataScience
