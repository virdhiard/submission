#Menyiapkan DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set_theme(style='dark')

day_df = pd.read_csv("day_data.csv")

#Membuat berbagai visualisasi data

st.header("Bike Sharing Dashboard")

#Visualisasi Pengguna Sepeda Saat Libur dan Hari Kerja
st.subheader('Pengguna Sepeda Saat Libur dan Hari Kerja')

workingday_data = day_df.groupby(by="workingday").agg({
    "casual": ["mean", ],
    "registered": ["mean", ],
    "cnt": ["mean", ]
})

fig, ax = plt.subplots(figsize=(50, 30))

workingday_data.plot(kind="bar", ax=ax)  # Menggunakan ax untuk plot

ax.set_xlabel("Hari Kerja (0: Libur dan Akhir Pekan, 1: Hari Kerja)", fontsize=40)
ax.set_ylabel("Rata-rata Jumlah Penyewa", fontsize=40)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Rotasi label sumbu x 
ax.legend(loc="upper left", fontsize=40)
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=40)

st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Berdasarkan bar chart diatas dapat disimpulkan bahwa lebih banyak orang 
        yang menyewa sepeda pada hari kerja secara keseluruhan (cnt) di karenakan 
        mayoritas orang yang menggunakan sepeda untuk bepergian ke sekolah maupun 
        bekerja sudah terdaftar pada aplikasi penyewa sepeda (registered). Sedangkan 
        untuk penyewa sepeda yang hanya menggunakan sepeda secara (casual) lebih 
        banyak menyewa pada hari libur atau akhir pekan karena digunakan untuk 
        jalan-jalan dan bepergian ke tempat wisata.
        """
    )

#Visualisasi Pengguna Sepeda Tiap Musim dan Bulannya
st.subheader('Pengguna Sepeda Setiap Musim dan Bulan')

season_data = day_df.groupby(by="season").agg({
    "casual": ["mean"],
    "registered": ["mean"],
    "cnt": ["mean"]
})

fig, ax = plt.subplots(figsize=(50, 30))

season_data.plot(kind="bar", ax=ax)  # Menggunakan ax untuk plot


ax.set_title("Musim Panas Menjadi Musim Favorit Bagi Penyewa Sepeda", fontsize=40)
ax.set_xlabel("Musim (1: Winter, 2: Spring, 3: Summer, 4: Autumn)", fontsize=40)
ax.set_ylabel("Rata-rata Jumlah Penyewa", fontsize=40)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Rotasi label sumbu x 
ax.legend(loc="upper left", fontsize=40)
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=40)

st.pyplot(fig)

month_data = day_df.groupby(by="month").agg({
    "cnt": ["mean"]
})

fig, ax = plt.subplots(figsize=(50, 30))

month_data.plot(kind="bar", ax=ax)  # Menggunakan ax untuk plot

ax.set_title("Jumlah Penyewa Sepeda Terbanyak Terjadi pada Bulan Juni", fontsize=40)
ax.set_xlabel("Bulan", fontsize=40)
ax.set_ylabel("Rata-rata Jumlah Penyewa", fontsize=40)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Rotasi label sumbu x 
ax.legend(loc="upper left", fontsize=40)
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=40)

st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Terdapat kecenderungan pengguna untuk menyewa pada musim panas karena 
        kondisi suhu yang nyaman untuk bersepeda baik itu untuk bekerja dan sekolah 
        maupun jalan-jalan keliling kota. Musim dingin menjadi musim paling sedikit 
        orang menyewa sepeda karena kondisi suhu yang dingin dan berangin. Selain 
        itu, kondisi jalan yang licin membuat orang lebih memilih menggunakan 
        transportasi lain. Dan pada bulan Juni dan September menjadi Bulan paling 
        banyak orang menyewa sepeda dan menggunakannya untuk berbagai aktivitasnya.
        """
    )