import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header('Bike Sharing Dashboard 🚲')

# Menyiapkan data (Load data bersih yang tadi di-download dari Colab)
df = pd.read_csv("dashboard/main_data.csv")

# 3. Menampilkan ringkasan data di Sidebar (Opsional tapi keren)
with st.sidebar:
    st.image("assets/sepeda.jpg")
    st.write("Analisis Penyewaan Sepeda")

# 4. Membuat Visualisasi 1: Berdasarkan Musim
st.subheader('Penyewaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='season', y='cnt', data=df, ax=ax)
st.pyplot(fig)

# 5. Membuat Visualisasi 2: Berdasarkan Cuaca
st.subheader('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax)
st.pyplot(fig)

st.caption('Copyright (c) Vina 2026')