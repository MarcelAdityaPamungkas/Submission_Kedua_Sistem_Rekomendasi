# Laporan Proyek Machine Learning - Marcel Aditya Pamungkas

## Project Overview

Musik menjadi salah satu aspek penting bagi sebagian orang di dunia ini. Pada abad ke-19, musik mulai banyak dibuat dengan alat-alat musik yang masih terbilang tradisional dan kuno. 

## Business Understanding

### Problem Statements
1. Genre lagu apa yang favorit di kalangan masyarakat umum? Siapa penyanyi paling populer menurut orang-orang dalam data tersebut?
2. Bagaimana cara agar baik pengguna maupun penyedia dapat selalu tertarik untuk mendengarkan musik?
3. Bagaimana cara membuat sistem rekomendasi terbaik yang dapat diimplementasikan?

### Goals
1. Mengetahui genre lagu maupun penyanyi paling populer, serta mencari hubungan antar variabel yang berkaitan dengan musik.
2. Membuat berbagai fitur yang mudah namun menarik, salah satunya adalah sistem rekomendasi.
3. Menggunakan algoritma cosine similarity maupun pemodelan machine learning untuk membuat sistem rekomendasi, lalu mengevaluasi menggunakan untuk menjamin keakuratan sistem rekomendasi.

### Solution Approach
1. Mengimplementasikan Exploratory Data Analysis (EDA) untuk analisis dan visualisasi data.
2. Mengimplementasikan content-based filtering approach menggunakan algoritma cosine similarity.
3. Mengimplementasikan collaborative-based filtering approach menggunakan algoritma deep learning.

## Data Understanding
Dataset yang digunakan untuk membuat sistem rekomendasi lagu diambil dari platform kaggle dengan dataset dapat diakses pada link [berikut](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/data). Dataset dipublikasikan oleh MaharshiPandya dengan usability 10/10. Data ini didapat dari spotify yang terdiri dari 1 file csv.

### Keterangan Variabel

Dataset ini memiliki 20 variabel dengan keterangan sebagai berikut.

Variabel | Keterangan
----------|----------
track_id | ID lagu pada Spotify
artists | Penyanyi pada lagu
album_name | Nama album lagu
track_name | Judul lagu
popularity | Tingkat popularitas lagu dalam skala 0 - 100 (0 = tidak populer, 100 = sangat populer)
duration_ms | Durasi lagu dalam satuan milidetik
explicit | Apakah lagu memiliki lirik eksplisit
danceability | Tingkat kesesuaian lagu untuk menari dalam skala 0 - 1 (0 = tidak cocok, 1 = sangat cocok)
energy | Tingkat energi pada lagu dalam skala 0 - 1 (0 = tidak berenergi, 1 = sangat berenergi)
key | Kunci not pada lagu
loudness | Tingkat kekerasan suara dalam satuan desibel
mode | Mode pada lagu (0 = minor, 1 = mayor)
speechiness	| Tingkat kata yang diucapkan dalam skala 0 - 1 (0 = tidak ada, 1 = hanya berisi kata)
acousticness | Tingkat akustik pada lagu dalam skala 0 - 1 (0 = tidak ada, 1 = pasti ada)
instrumentalness | Tingkat instrumental pada lagu dalam skala 0 - 1 (0 = Bukan instrumental, 1 = instrumental)
liveness | Tingkat kehadiran audience pada saat lagu dinyanyikan dalam skala 0 - 1 (0 = tidak ada, 1 = ada)
valence | Jenis transportasi yang digunakan
tempo | Tempo lagu dalam beat per menit
time_signature | Tanda birama pada lagu
track_genre | Genre lagu
