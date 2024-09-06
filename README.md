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

### Statistik Data

Selanjutnya akan ditampilkan statistik data numerikal secara umum.

popularity | duration_ms | danceability	| energy | key | loudness | mode | speechiness | cousticness | instrumentalness | liveness | valence | tempo | time_signature
----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------
count |	114000 | 114000 | 114000 | 114000 | 114000 | 114000 | 114000 | 114000	| 114000 | 114000 | 114000 | 114000 | 114000 | 114000
mean | 33.238535 | 2.280292e+05	| 0.566800 | 0.641383 |	5.309140 | -8.258960 | 0.637553	| 0.084652 | 0.314910	| 0.156050 | 0.213553 |	0.474068 | 122.147837	| 3.904035
std	| 22.305078	| 1.072977e+05 | 0.173542 | 0.251529 | 3.559987	| 5.029337 | 0.480709	| 0.105732 | 0.332523	| 0.309555 | 0.190378	| 0.259261 | 29.978197 | 0.432621
min	| 0.000000 | 0.000000e+00	| 0.000000 | 0.000000	| 0.000000 | -49.531000	| 0.000000 | 0.000000 | 0.000000 | 0.000000	| 0.000000 | 0.000000	| 0.000000 | 0.000000
25%	| 17.000000	| 1.740660e+05 | 0.456000	| 0.472000 | 2.000000	| -10.013000 | 0.000000	| 0.035900 | 0.016900	| 0.000000 | 0.098000	| 0.260000 | 99.218750 | 4.000000
50%	| 35.000000	| 2.129060e+05 | 0.580000	| 0.685000 | 5.000000	| -7.004000	| 1.000000 | 0.048900	| 0.169000 | 0.000042	| 0.132000 | 0.464000	| 122.017000 | 4.000000
75%	| 50.000000	| 2.615060e+05 | 0.695000	| 0.854000 | 8.000000	| -5.003000	| 1.000000 | 0.084500	| 0.598000 | 0.049000	| 0.273000 | 0.683000	| 140.071000 | 4.000000
max	| 100.000000 | 5.237295e+06 | 0.985000 | 1.000000 |	11.000000	| 4.532000 | 1.000000	| 0.965000 | 0.996000 | 1.000000 | 1.000000	| 0.995000 | 243.372000	| 5.000000

### Exploratory Data Analysis (EDA)

Dari variabel-variabel yang diketahui, variabel dapat dibagi menjadi 2 jenis, yaitu variabel numerikal dan variabel kategorikal. Berikut merupakan kolom-kolom yang termasuk dalam variabel numerikal maupun kategorikal.\
Kolom-kolom numerikal: [`popularity`, `duration_ms`,	`danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`,	`acousticness`, `instrumentalness`, `liveness`, `valence tempo`, `time_signature`]\
Kolom-kolom kategorikal: [`explicit`, `track_genre`]\
Sementara kolom-kolom lainnya yaitu [`track_id`, `artists`, `album_name`, `track_name`] tidak dapat dikategorikan. 

#### Analisis Kolom `Explicit`

<img src = "gambar/Analisis_Kategorikal.png"/> <br>
