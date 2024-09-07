# Laporan Proyek Machine Learning - Marcel Aditya Pamungkas

## Project Overview

Musik menjadi salah satu aspek penting bagi sebagian orang di dunia ini. Pada abad ke-19, musik mulai banyak dibuat dengan alat-alat musik yang masih terbilang tradisional dan kuno. 

## Business Understanding

### Problem Statements
1. Apa genre lagu yang paling favorit di kalangan masyarakat umum?
2. Siapa penyanyi paling populer menurut orang-orang dalam data tersebut?
3. Apakah ada hubungan antar variabel pada dataset yang dapat diinterpretasikan?
4. Bagaimana cara agar baik pengguna maupun penyedia dapat selalu tertarik untuk mendengarkan musik?
5. Bagaimana cara membuat sistem rekomendasi terbaik yang dapat diimplementasikan?

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
valence | Tingkat perasaan pada lagu dalam skala 0 - 1 (0 = Negatif (sedih, marah), 1 = Positif (senang, euforia)
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

#### 1. Analisis Kolom `Explicit`

<img src = "gambar/01. Distribusi Kolom Explisit.png"/> <br>

Dari gambar di atas, hanya 8.55% dari seluruh lagu pada dataset yang memiliki lirik bersifat eksplisit. 

#### 2. Distribusi Kolom Numerikal Menggunakan Histogram

<img src = "gambar/02. Histogram dari Kolom Numerikal.png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Kolom `danceability`, `valence`, dan `tempo` mendekati distribusi normal. Kolom `popularity` juga mendekati distribusi normal, namun mayoritas data bernilai 0.
* Kolom `loudness` memiliki histogram yang bersifat left-skewed. Artinya mayoritas data bernilai tinggi, yang berarti banyak musik memiliki `loudness` sekitar -15 hingga 0 dB.
* Kolom `speechiness`, `acousticness`, dan `liveness` memiliki histogram yang bersifat right-skewed. Artinya mayoritas data pada kolom-kolom tersebut bernilai rendah.
* Kolom `energy` memiliki distribusi yang semakin tinggi untuk tingkat energi yang semakin tinggi.
* Kolom `duration_ms` menunjukkan mayoritas lagu memiliki durasi dibawah 1000000 milidetik.
* Kolom `mode` hanya memiliki 2 nilai data, yaitu 0 dan 1, sesuai dengan arti dari `mode`. Nilai 1 lebih banyak dari 0 yang menunjukkan mayoritas lagu menggunakan skala mayor.
* Kolom `instrumentalness` memiliki nilai mayoritas mendekati yang berarti mayoritas lagu bukan merupakan instrumental (hanya berisi iringan musik tanpa lirik).

#### 3. Korelasi Antar Variabel Numerikal Menggunakan Heatmap

Sebelum melihat korelasi dari seluruh variabel numerik, akan ditetapkan batasan nilai korelasi beserta artinya. Misalkan $x$ merupakan nilai korelasi suatu variabel
* Korelasi bernilai $0.00 \leq x \leq 0.30$ dan $-0.30 \leq x \leq 0.00$ merupakan korelasi yang bersifat sangat lemah. Artinya, variabel-variabel tersebut memiliki keterkaitan yang kecil atau bahkan tidak ada kaitan.
* Korelasi bernilai $0.31 \leq x \leq 0.60$ dan $-0.60 \leq x \leq -0.31$ merupakan korelasi yang bersifat cukup kuat. Artinya, variabel-variabel tersebut memiliki keterkaitan yang cukup kuat satu sama lain.
* Korelasi bernilai $0.61 \leq x \leq 1.00$ dan $-1.00 \leq x \leq -0.61$ merupakan korelasi yang bersifat sangat kuat. Artinya, variabel-variabel tersebut memiliki keterkaitan yang kuat atau bahkan sangat kuat.

Berdasarkan 3 tingkatan tersebut, korelasi dibagi menjadi 2, yaitu korelasi positif dan korelasi negatif.
* Korelasi positif merupakan korelasi yang bernilai $0.00 <x \leq 1.00$. Artinya, semakin tinggi nilai salah satu variabel, maka nilai variabel lainnya juga akan semakin tinggi. Hal ini berlaku sebaliknya.
* Korelasi positif merupakan korelasi yang bernilai $-1.00 <x \leq 0.00$. Artinya, semakin tinggi nilai salah satu variabel, maka nilai variabel lainnya justru akan semakin rendah. Hal ini berlaku sebaliknya.

Berikut merupakan heatmap dari kolom-kolom numerikal pada dataset.

<img src = "gambar/03. Heatmap Kolom Numerikal.png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Variabel `danceability` berkorelasi positif yang cukup kuat terhadap variabel `valence`
* Variabel `energy` berkorelasi positif yang kuat terhadap variabel `loudness`, namun berkorelasi negatif yang kuat terhadap variabel `acousticness`
* Variabel `loudness` berkorelasi negatif yang cukup kuat terhadap variabel `acousticness` dan variabel `instrumentalness`
* Variabel `instrumentalness` berkorelasi negatif yang cukup kuat terhadap variabel `valence`

Selain yang disebutkan di atas, seluruh variabel memiliki korelasi yang lemah antara satu dengan yang lain. Selanjutnya, akan dilihat variabel-variabel yang berkorelasi dengan variabel lainnya.

#### 4. Korelasi Variabel `danceability` dengan `valence`

<img src = "gambar/04. Scatter Plot (1).png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Terlihat bahwa variabel `danceability` berkorelasi positif yang cukup kuat terhadap variabel `valence`, terlihat dari garis yang mengarah ke atas kanan.
* Kedua variabel ini berkorelasi positif cukup kuat karena lagu yang memiliki perasaan positif seperti senang tentu juga cocok untuk menari.
* Akan aneh apabila lagu sedih bisa digunakan untuk menari, sehingga dapat dilihat bahwa lagu yang yang memang memiliki perasaan negatif seperti sedih dan marah tidak cocok untuk menari.

#### 5. Korelasi Variabel `energy` dengan `loudness` dan `acousticness`

<img src = "gambar/05. Scatter Plot (2).png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Terlihat bahwa variabel `energy` berkorelasi positif yang kuat terhadap variabel `loudness`, terlihat dari garis yang mengarah ke atas kanan, tetapi berkorelasi negatif yang cukup kuat terhadap variabel `acousticness`, terlihat dari garis yang mengarah ke bawah kanan.
* Secara umum, semakin keras suara lagu tersebut, semakin berenergi lagu tersebut, terutama pada genre seperti metal music. Oleh karena itu, variabel `energy` dan `loudness` berkorelasi positif yang kuat.
* Sementara itu, lagu akustik biasanya menggunakan alat musik akustik yang tentu suaranya lebih pelan dibanding alat musik elektrik, serta lagu akustik biasa dinyanyikan dengan suara yang pelan, indah, dan tanpa batuan mikrofon. Akibatnya, jika lagu tersebut merupakan akustik, tentu energinya lebih rendah dibanding lagu non akustik. Oleh karena itu, variabel `energy` dan `acousticness` berkorelasi negatif yang cukup kuat.

#### 6. Korelasi Variabel `loudness` dengan `acousticness` dan `instrumentalness`

<img src = "gambar/06. Scatter Plot (3).png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Terlihat bahwa variabel `loudness` berkorelasi negatif yang cukup kuat terhadap variabel `acousticness` dan `instrumentalness`, terlihat dari garis yang mengarah ke bawah kanan.
* Seperti pada pembahasan sebelumnya, lagu akustik cenderung memiliki suara yang pelan dan indah sehingga suaranya tidak kencang.
* Selain itu, musik yang hanya instrumental (hanya iringan alat musik tanpa lirik) cenderung memiliki suara konstan yang cukup kencang dibandingkan dengan musik non instrumental yang iringan musiknya akan sedikit pelan ketika lirik lagu dinyanyikan.

#### 7. Korelasi Variabel `instrumentalness` dengan `valence`

<img src = "gambar/07. Scatter Plot (4).png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Terlihat bahwa variabel `instrumentalness` berkorelasi negatif yang cukup kuat terhadap variabel `valence`, terlihat dari garis yang mengarah ke bawah kanan.
* Biasanya, suasana ceria dalam lagu dibawakan bersamaan dengan nyanyian lirik lagu. Sementara suasana negatif, terutama sedih, dibawakan hanya dalam bentuk instrumental (contohnya dengan violin saja)

#### 8. Top 10 Album dengan Jumlah Musik Terbanyak

<img src = "gambar/08. Top 10 Album.png"/> <br>

Dari gambar di atas, album `Alternative Christmas 2022` merupakan album yang memiliki jumlah lagu terbanyak, hingga mendekati 200 lagu.

#### 9. Analisis Genre Musik

Setelah mencari jumlah data unik pada kolom `track_genre` dengan `unique_genres = data["track_genre"].unique()`, didapat 114 genre yang ada di dalam dataset tersebut. Selanjutnya, akan dianalisis beberapa kolom berdasarkan genrenya.

<img src = "gambar/09. Top 10 Genre.png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Pada gambar `Top 10 Jumlah Penyanyi Pada Setiap Genre`, genre dubstep merupakan genre yang memiliki artis terbanyak, berjumlah lebih dari 700.
* Pada gambar `Jumlah Lagu pada Top 0.1% Berdasarkan Genre`, genre pop memiliki jumlah lagu terbanyak pada top 0.1% lagu dengan jumlah lebih dari 20.
* Pada gambar `Top 10 Genre dengan Rasio Rata-Rata Eksplisit Tertinggi`, genre komedi merupakan genre yang memiliki rasio lirik eksplisit tertinggi dibandingkan genre lainnya dengan rasio sekitar 0.65.
* Pada gambar `Top 10 Genre dengan Rata-Rata Popularitas Tertinggi`, genre pop-film merupakan genre yang memiliki popularitas tertinggi secara rata-rata dibandingkan dengan genre lainnya, mendekati skor 60.

#### 10. Analisis Penyanyi

Setelah mencari jumlah data unik pada kolom `artists` dengan `unique_artist = data["artists"].unique()`, didapat 31437 penyanyi yang ada di dalam dataset tersebut. Selanjutnya, akan dicari top 10 dari beberapa kolom berdasarkan penyanyinya.

<img src = "gambar/10. Top 10 Penyanyi.png"/> <br>

Gambar di atas dapat diinterpretasikan sebagai berikut.
* Pada gambar `Top 10 Penyanyi dengan Jumlah Lagu terbanyak`, The Beatles telah membuat lagu terbanyak dibandingkan penyanyi lainnya, yaitu lebih dari 250.
* Pada gambar `Top 10 Penyanyi dengan Rata-Rata Popularitas Tertinggi`, Sam Smith dan Kim Petras memiliki nilai popularitas tertinggi dibandingkan penyanyi lainnya, yaitu mendekati 100.

## Data Preparation

Karena data yang digunakan sedikit berbeda antara content-based filtering dengan collaborative filtering, maka data preparation dari kedua approach tersebut akan dilakukan secara masing-masing.

### 1. Content-Based Filtering
Untuk content-based filtering, kita akan fokus pada judul lagu beserta genre dari lagu tersebut. Oleh karena itu, kita hanya akan mengambil 4 kolom dari data yang dimiliki, yaitu
* `track_id`
* `track_name`
* `album_name`
* `track_genre`

Selanjutnya, digunakan TfidfVectorizer() pada genre lagu untuk menghasilkan output berupa angka antara 0 - 1. Lalu, dibentuk dataframe yang berisi genre lagu yang telah dilakukan vektorisasi dengan TfidfVectorizer() sebagai kolom dan seluruh judul lagu sebagai barisnya. Hal ini dilakukan karena akan digunakan cosine similarity pada content-based filtering, dimana cosine similarity memerlukan bentuk angka agar dapat dihitung. Contoh dari dataframe dapat dilihat pada tabel berikut.

| track_name | acoustic |	afrobeat | age | alt | alternative | ambient | and | anime | bass |	black	| ... | swedish |	synth	| tango	| techno | tonk |	trance | trip |	tunes |	turkish	| world |
| --------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Comedy | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.000000 |
| Ghost - Acoustic | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.000000 |
| To Begin Again | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.000000 |
| Can't Help Falling In Love | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.000000 |
| Hold On	| 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.000000 |
| ...	| ... |	...	| ...	| ...	| ... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |	... |
| Sleep My Little Boy	| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.707107 |
| Water Into Light | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.707107 |
| Miss Perfumado | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.707107 |
| Friends | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.707107 |
| Barbincor | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.707107 |

### 2. Collaborative Filtering
Untuk collaborative filtering, kita juga akan fokus pada judul lagu beserta genre dari lagu tersebut. Berbeda dengan content-based, kita hanya akan mengambil 3 kolom dari data yang dimiliki, yaitu
* `track_id`
* `track_name`
* `popularity`

Karena `track_id` dan `track_name` memiliki tipe data string dan unik, maka dilakukan encoding terhadap kedua kolom tersebut, kemudian dibentuk dataframe yang berisi kolom `track_id` yang sudah diencoding, kolom `track_name` yang sudah diencoding, dan `popularity`. Contoh dari dataframe dapat dilihat pada tabel berikut.

| No | track | name | popularity |
|-----|-----|-----|-----|
| 113186 | 88965 | 72967 | 50.0 |
| 42819 |	38267	| 32043 | 11.0 |
| 59311 |	50834	| 42419 |	0.0 |
| 90417 |	10752	| 9489 | 34.0 |
| 61000 |	52275	| 43640 |	57.0 |

Setelah data yang diperlukan telah diencoding, selanjutnya data dibagi menjadi dua, yaitu data training dan data testing untuk pembuatan dan pelatihan model. Data training digunakan untuk melatih model dengan data yang ada, sedangkan data testing digunakan untuk menguji model yang dibuat menggunakan data yang belum dilatih. Pembagian data ini dilakukan dengan perbandingan 80% : 20% untuk data training dan data testing.

## Modelling and Result

### 1. Content-Based Filtering

Content-based filtering menggunakan cosine similarity sebagai algoritma untuk membuat sistem rekomendasi berdasarkan content-based filtering approach. Cosine similarity mengukur kesamaan antara dua vektor dan menentukan apakah kedua vektor tersebut menunjuk ke arah yang sama. Ia menghitung sudut cosinus antara dua vektor. Semakin kecil sudut cosinus, semakin besar nilai cosine similarity. Cosine similarity dirumuskan sebagai berikut.

$$Cos (\theta) = \frac{\sum_1^n a_ib_i}{\sqrt{\sum_1^n a_i^2}\sqrt{\sum_1^n b_i^2}}$$

Pada python, kita akan menggunakan  `cosine_similarity` untuk mendapatkan nilai cosinus dua vektor dalam matriks. Cosine similarity memiliki kelebihan seperti output yang ternormalisasi (rentang -1 hingga 1) sehingga memudahkan interpretasi, penggunaan yang mudah dan sederhana, serta efisien untuk data sparse berdimensi tinggi, seperti TF-IDF. Meski demikian, cosine similarity memiliki beberapa kelemahan, seperti menganggap seluruh faktor/parameter sama penting, sensitif terhadap perubahan 'sudut vektor', dan tidak selalu cocok untuk data negatif. Setelah dibentuk sistem rekomendasi, selanjutnya akan diuji sistem rekomendasi ini untuk menampilkan top 10 rekomendasi berdasarkan lagu yang didengar/dipilih oleh user. Diperoleh hasil berikut.

`content_based_music_recommendations('Fire - Killer Hertz Remix')`

| No | track_name |	track_id | album_name |	track_genre |
|-----|-----|-----|-----|-----|
| 0 |	Lilith's Club	| 4LqkHTCD7pwRtSkrIQSwk2 | Devil May Cry (Original Game Soundtrack)	| breakbeat |
| 1	| Lilith's Club	| 4LqkHTCD7pwRtSkrIQSwk2 | Devil May Cry (Original Game Soundtrack)	| drum-and-bass |
| 2	| Golden | 6PvyiMpxf25jjnZdF4DKIG	| Commix Presents Dusted (Selected Works 2003 - ...	| drum-and-bass |
| 3	| Golden | 5qtyotxUJIumSIkklcJL50	| Golden | dubstep |
| 4	| Golden | 4ptzVhD7TWh4aBkhWEzz0o	| Darkbloom |	metalcore |
| 5	| Find Me |	6xB7E0HOWznwiO0v56mqwD | Find Me | drum-and-bass |
| 6	| Find Me | 0hQnWNnpCxU7dE1BkCAbXt | Hope	| drum-and-bass |
| 7	| Find Me |	73zHDJiSMd6wCpxKNWWEPy | Find Me | groove |
| 8	| Find Me |	6aWiGv6hPG0o3ri7QHNs8t | Joytime | progressive-house |
| 9	| Engine Room |	00btR3u8FwO3Ip97Az3nZM | Drum & Bass Summer Slammers: 2012 Sampler | drum-and-bass |

### 2. Collaborative Filtering

Collaborative Filtering menggunakan deep learning, tepatnya embedding layer untuk membuat model deep learning. Embedding layer merupakan tipe layer pada deep learning yang digunakan untuk mentransformasikan data kategorikal menjadi vektor dengan nilai kontinu. Pada python, kita menggunakan `tensorflow.keras.layers Embedding` untuk membentuk embedding layer. Embedding Layer memiliki kelebihan seperti mengurangi kompleksitas model, dapat digunakan di berbagai macam algoritma deep learning, dan menangkap hubungan semantic pada data. Meski demikian, embedding layer juga memiliki beberapa kelemahan, seperti membutuhkan data yang banyak, sensitif terhadap hyperparameter, dan cold start problem. Setelah model dibentuk dan dilatih, diperoleh hasil `root_mean_squared_error: 0.0303` untuk data training dan `val_root_mean_squared_error: 0.1892` untuk data testing. Nilai tersebut sudah bagus untuk digunakan dalam sistem rekomendasi, sehingga dapat dibentuk sistem rekomendasi berdasarkan model tersebut. Selanjutnya, akan diuji sistem rekomendasi ini untuk menampilkan top 10 rekomendasi berdasarkan lagu yang didengar/dipilih oleh user. Diperoleh hasil berikut.

`recommend_tracks_based_on_track_name("Fire - Killer Hertz Remix", top_n = 10)`

Rekomendasi berdasarkan track dengan judul: 'Fire - Killer Hertz Remix'\
10 Rekomendasi Terbaik:\
ID Track: 18asYwWugKjjsihZ0YvRxO, Judul Track: The Motto\
ID Track: 2dpaYNEQHiRxtZbfNsse99, Judul Track: Happier\
ID Track: 4zN21mbAuaD0WqtmaTZZeP, Judul Track: Ferrari\
ID Track: 4h9wh7iOZ0GGn8QVp4RAOB, Judul Track: I Ain't Worried\
ID Track: 0lYBSQXN6rCTvUZvg9S0lU, Judul Track: Let Me Love You\
ID Track: 48AJSd42lXpicsGqcgopof, Judul Track: X ÚLTIMA VEZ\
ID Track: 6f3Slt0GbA2bPZlz0aIFXN, Judul Track: The Business\
ID Track: 3kUq4sBcmxhnOtNysZ9yrp, Judul Track: Feliz Cumpleaños Ferxxo\
ID Track: 7e89621JPkKaeDSTQ3avtg, Judul Track: Sweet Home Alabama\
ID Track: 6GG73Jik4jUlQCkKg9JuGO, Judul Track: The Middle
