import streamlit as st
import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io
import os
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from tensorflow.keras.utils import get_file

def add_custom_header():
    html_code = """
    <html>
    <body margin: 20px;">
        <div style="text-align: center; margin-top: 30px; padding: 10px"> 
            <img src="https://raw.githubusercontent.com/alberanalafean22/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/Logo1.png" alt="Logo 1" width="85" height="85">    
            <img src="https://raw.githubusercontent.com/alberanalafean22/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/Logo2.png" alt="Logo 2" width="85" height="85"> 
            <img src="https://raw.githubusercontent.com/alberanalafean22/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/Logo3.png" alt="Logo 3" width="85" height="85">
            <img src="https://raw.githubusercontent.com/alberanalafean22/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/Logo0.png" alt="Logo kelompok" width="85" height="85">
        </div>
        <div class="header" style="text-align: center; margin-top: 30px; padding: 10px">
            <h1 style="font-size: 35px; tyle="text-align: center; margin-top: 20px;">
                AVCLA (Aves Classification)
            </h1>
            <h4 style="font-size: 28px; margin-top: 20px;">
                Implementasi Model Transfer Learning Arsitektur ConvNeXt untuk Klasifikasi Suara Burung di Taman Nasional Way Kambas
            </h4>
        </div>
    </body>
    </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)
add_custom_header()





import gdown
import tensorflow as tf

# Corrected Google Drive URL
drive_url = "https://drive.google.com/uc?id=1HNV0talV3HDmtkYUFZ6u0_hrugPcF4uc"

# Output path for the downloaded file
output_path = "convnextaugmentasiepochs50.keras"

# Download file from Google Drive
print("Downloading model from Google Drive...")
gdown.download(drive_url, output_path, quiet=False)

# Load model using TensorFlow
print("Loading model with TensorFlow...")
try:
    model = tf.keras.models.load_model(output_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Failed to load the model: {e}")









# Kelas untuk klasifikasi
class_indices = {
    'Cacomantis Merulinus': 0,
    'Culicicapa Ceylonensis': 1,
    'Geopelia Striata': 2,
    'Halcyon Smyrnensis': 3,
    'Ninox Scutulata': 4,
    'Orthotomus Ruficeps': 5,
    'Pitta Sordida': 6,
    'Prinia Flaviventris': 7,
    'Spilopelia Chinensis': 8,
    'Surniculus Lugubris': 9
}
class_labels = {v: k for k, v in class_indices.items()}

# Fungsi untuk memproses file audio menggunakan librosa
def preprocess_audio(file):
    # Membaca file audio menggunakan librosa
    audio, sr = librosa.load(file, sr=16000)  # Mengatur sample rate menjadi 16000 Hz
    
    # Menghitung energi audio (energi rata-rata per frame)
    energy = np.square(audio).mean(axis=0)
    
    # Tentukan ambang batas energi untuk mendeteksi segmen dengan energi tinggi
    threshold = np.percentile(energy, 90)  # Ambang batas di persentil 90 untuk energi tinggi
    
    # Ambil indeks frame dengan energi tinggi
    high_energy_frames = np.where(energy > threshold)[0]
    
    # Tentukan durasi 5 detik (16000 frame untuk 16000 Hz)
    segment_duration = 16000 * 5  # 5 detik
    
    # Ambil 5 detik dari segmen dengan energi tinggi
    if len(high_energy_frames) > segment_duration:
        high_energy_audio = audio[high_energy_frames[0]:high_energy_frames[segment_duration]]
    else:
        high_energy_audio = audio[:segment_duration]  # Jika kurang dari 5 detik, ambil sisa audio
    
    return high_energy_audio, sr


# Fungsi untuk mengonversi audio menjadi Mel-spectrogram
def audio_to_melspectrogram(high_energy_audio, sr):
    # Mengubah audio menjadi Mel-spectrogram menggunakan librosa
    melspec = librosa.feature.melspectrogram(y=high_energy_audio, sr=sr, n_fft=1024, hop_length=512, n_mels=128)
    melspec_db = librosa.power_to_db(melspec, ref=np.max)

    # Membuat visualisasi dari Mel-spectrogram
    fig = plt.figure(figsize=(5, 5))
    plt.axis('off')
    plt.imshow(melspec_db, aspect='auto', origin='lower', cmap='inferno')
    canvas = FigureCanvas(fig)
    buf = io.BytesIO()
    canvas.print_png(buf)
    plt.close(fig)
    buf.seek(0)
    return buf

# Fungsi untuk menyiapkan gambar untuk input model
def prepare_image(image_buf):
    # Menyiapkan gambar untuk input model
    img = image.load_img(image_buf, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Fungsi untuk menambahkan background ke halaman Streamlit
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1444464666168-49d633b86797?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-position: top center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Menambahkan background
add_bg_from_url()

# File uploader untuk audio
uploaded_file = st.file_uploader("Upload File Audio disini (!format mp3)", type=["mp3"])

if uploaded_file:
    # Proses file audio
    high_energy_audio, sr = preprocess_audio(uploaded_file)
    
    # Konversi audio menjadi Mel-spectrogram
    spectrogram_buf = audio_to_melspectrogram(high_energy_audio, sr)

    # Menyiapkan gambar untuk input model
    img_array = prepare_image(spectrogram_buf)

    # Prediksi menggunakan model
    predicted_probabilities = model.predict(img_array, verbose=0)
    predicted_class = np.argmax(predicted_probabilities, axis=1)[0]

    # Ambil kelas dan akurasi
    kelas = class_labels.get(predicted_class, "Unknown")
    akurasi = predicted_probabilities[0][predicted_class] * 100

    # Menampilkan hasil prediksi
    st.metric(label="Kelas Terprediksi", value=kelas)
    st.metric(label="Akurasi Prediksi", value=f"{akurasi:.2f}%")

    # Menampilkan gambar sesuai kelas
    if kelas == 'Cacomantis Merulinus':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/a.png"
    elif kelas  == 'Culicicapa Ceylonensis':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/b.png"
    elif kelas  == 'Geopelia Striata':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/c.png"
    elif kelas  == 'Halcyon Smyrnensis':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/d.png"
    elif kelas  == 'Ninox Scutulata':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/e.png"
    elif kelas  == 'Orthotomus Ruficeps':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/f.png"
    elif kelas  == 'Pitta Sordida':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/g.png"
    elif kelas  == 'Prinia Flaviventris':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/h.png"
    elif kelas  == 'Spilopelia Chinensis':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/i.png"
    elif kelas  == 'Surniculus Lugubris':
        image_url = "https://raw.githubusercontent.com/deeplearning13projectsd/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/kelas/j.png"

    st.image(image_url, caption=f"Kelas: {kelas}", use_container_width=True)


def add_custom_footer():
    html_code = """
    <html>
    <body>
        <div class="footer" style="text-align: center; margin-top: 30px; padding: 10px">
            <h5 style="margin: 5px 0;">AVCLA</h5>
            <p style="margin: 5px 0;">AVCLA (Aves Classification), merupakan sebuah website dalam mendeteksi klasifikasi burung di kawasan Taman Nasional Way Kambas. Website ini bisa mendeteksi klasifikasi pada 10 spesies burung, dengan memanfaatkan metode Deep Learning menggunakan Transfer Learning dengan arsitektur Convnext Type Base. Website ini bisa memprediksi spesies burung berdasarkan suara. Model ini dibangun dalam memenuhi Case Based Learning pada matakuliah SD4102Deep Learning di Program Studi Sains Data.</p>
            <h4>‎‎‎‎‎‎‎‎ㅤ</h4>
            <h5 style="margin: 0;">© Developer: Kelompok 13 Deep Learning</h5>
            <img src="https://raw.githubusercontent.com/alberanalafean22/DeteksiKlasifikasiSpesiesBurung/main/Deployment/asset/Logo0.png" alt="Logo kelompok" width="85" height="85">
            <h5 style="margin: 5px 0;">Version 1.0.1 December 2024</h5>
            <p>
                <a href="https://github.com/sains-data/Implementasi-Model-Transfer-Learning-Arsitektur-ConvNeXt-untuk-Klasifikasi-Suara-Burung-di-TNWK" target="_blank">
                    Visit the Our GitHub Repository
                </a>
            </p>
      </div>
    </body>
    </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)

add_custom_footer()
