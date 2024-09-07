# -*- coding: utf-8 -*-
"""Proyek_Kedua_Music_Recommendation_System

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10icpX_6D2V2euHgTqdW4MytbgcOhcADd

# 1. Mengimpor Library

Pada tahap ini, kita mengimpor seluruh library yang diperlukan, seperti numpy, pandas, seaborn, matplotlib, dan sklearn.
"""

import textwrap
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""# 2. Data Loading

Selanjutnya, kita melihat 10 baris pertama dari data dengan `.head()` dan ukuran dari data dengan `.shape`.
"""

data = pd.read_csv("/content/music_dataset.csv", index_col = 0)

# Menampilkan sepuluh baris pertama pada data
data.head(10)

# Menampilkan jumlah baris dan kolom pada data
total_row, total_column = data.shape
print(f"Total of rows: {total_row}")
print(f"Total of column: {total_column}")

"""Dari hasil di atas, diperoleh data ini memiliki 20 kolom dan 114000 baris.

# 3. Deskripsi Variabel

## Arti Variabel

Berikut adalah arti dari variabel-variabel pada data tersebut.

Variabel | Keterangan
----------|----------
track_id | ID lagu pada Spotify
artists | Penyanyi/artis pada lagu tersebut, dipisahkan dengan `;` jika terdapat lebih dari 1 artis
album_name | Judul album yang dirilis
track_name | Judul lagu yang dirilis
popularity | Popularitas lagu dari skala 0-100 berdasarkan total lagu diputar
duration_ms | Durasi lagu dalam satuan milidetik
explicit | Indikasi lagu memiliki lirik yang eksplisit (true = iya, false = tidak)
danceability | Kecocokan lagu untuk menari dari skala 0-1, dengan 0 tidak cocok dan 1 sangat cocok
energy | Intensitas dan aktivitas pada lagu dari skala 0-1, dengan 0 sangat rendah dan 1 sangat tinggi
key | Kunci nada dalam lagu menggunakan notasi standar Pitch Class. Contohnya 0 = C, 1 = C#, 2 = D
loudness | Kekerasan suara pada lagu dalam satuan desibel (dB)
mode | Jenis skala konten melodi berasal, dengan 0 = minor dan 1 = major
speechiness	| Penggunaan kata yang sering diucapkan dari skala 0-1, dengan 0 jarang dan 1 sering
acousticness | Tingkat kepercayaan apakah lagu tersebut akustik atau tidak dari skala 0-1, dengan 0 tidak dan 1 iya
instrumentalness | Tingkat instrumental pada lagu dari skala 0-1, dengan 0 bukan dan 1 iya
liveness | Mendeteksi keberadaan penonton dalam lagu dari skala 0-1, dengan 0 tidak ada dan 1 ada
valence | Tingkat perasaan dalam lagu dari skala 0-1, dengan 0 negatif (sedih, marah) dan 1 positif (senang, euforia)
tempo | Tempo lagu dalam satuan beat per menit
time_signature | Jumlah beat per bagian. Contohnya jika 4, maka lagu tersebut menggunakan birama 4/4
track_genre | Genre dari lagu tersebut

## Memeriksa Tipe Variabel Beserta Jumlah
"""

data.info()

"""Dari hasil di atas, terdapat
* 9 kolom bertipe float
* 5 kolom bertipe integer
* 5 kolom bertipe object
* 1 kolom bertipe boolean

Selain itu, pada kolom artists, album_name, dan track_name terdapat 1 baris dengan nilai null. Hal ini akan diperiksa nanti pada bagian data cleaning.

## Menampilkan Deskripsi Statistik dari Data
"""

data.describe()

"""Dari hasil di atas, disimpulkan
* Terdapat lagu berdurasi 0 milidetik. Hal ini tidak mungkin, sehingga akan diperiksa pada data cleaning.
* Pada `key`, tidak ada yang bernilai -1 sehingga seluruh kunci lagu terdefinisi.
* Selain dua hal di atas, seluruh data lainnya terlihat normal.

# 4. Data Cleaning

## Memeriksa Nilai yang Kosong pada Data
"""

# Menjumlahkan nilai null yang ada pada data
pd.DataFrame({'Nilai yang Kosong':data.isnull().sum()})

"""Terlihat bahwa terdapat 3 kolom yang memiliki 1 baris dengan nilai kosong. Akan diperiksa apakah nilai null ini pada baris yang sama atau berbeda."""

# Menghitung nilai null pada masing-masing baris
nilai_null_per_baris = data.isnull().sum(axis = 1)
total_nilai_null = nilai_null_per_baris.value_counts().sort_index()

# Menampilkan baris yang memiliki nilai null beserta jumlahnya
for missing, row in total_nilai_null.items():
    print(f'{row} baris memiliki nilai null sebanyak {missing}')

# Menampilkan jumlah baris yang memiliki nilai null
total_baris_dengan_nilai_null = (data.isnull().any(axis = 1)).sum()
print(f'Total baris yang memiliki nilai null: {total_baris_dengan_nilai_null}')

"""Dari hasil di atas, nilai null terdapat pada 1 baris yang sama."""

# Menampilkan baris yang memiliki nilai null
data[data.isnull().any(axis = 1)]

"""Terlihat bahwa baris ini memiliki nilai null pada kolom `artists`, `album_name`, dan `track_name`. Selain itu, baris ini juga memiliki durasi 0 milidetik yang tentu tidak mungkin. Maka baris ini akan dihapus."""

# Menghapus baris yang memiliki nilai null pada data
data.drop(data[data.isnull().any(axis = 1)].index, inplace = True)

# Menampilkan jumlah baris dan kolom pada data setelah menghapus baris dengan nilai null
total_row, total_column = data.shape
print(f"Total of rows: {total_row}")
print(f"Total of column: {total_column}")

"""Selanjutnya, akan dilihat deskripsi statistik dari data setelah dihapus 1 baris."""

data.describe()

"""Berdasarkan hasil deskripsi statistik di atas, terlihat bahwa nilai-nilai di atas sudah sesuai dan mungkin terjadi, sehingga tidak akan diperiksa terkait outlier.

## Memeriksa Data Duplikat
"""

# Menghitung jumlah data duplikat
data.duplicated().sum()

"""Dari hasil di atas, terdapat 450 data duplikat. Akan diperiksa terlebih dahulu apakah data duplikat ini pada seluruh kolom."""

# Menampilkan data duplikat
data[data.duplicated]

"""Dari hasil di atas, terlihat bahwa tidak ada baris yang duplikat satu sama lain. Kemungkinan data dianggap duplikat karena terdapat beberapa kolom yang bernilai sama. Oleh karena itu, 450 data yang dianggap duplikat tidak akan dihapus. Data sudah siap untuk diproses dan dianalisis.

# 5. Exploratory Data Analysis (EDA)

Pertama, kita akan membagi variabel-variabel yang ada menjadi 2 kategori, yaitu kategori kategorical dan kategori numerikal.
"""

# Membentuk data berisi kolom-kolom kategorikal (data yang bertipe object dan bool)
kolom_kategorikal = data[data.columns[(data.dtypes == "object") | (data.dtypes == "bool")]]

# Menampilkan data kolom kategorikal
kolom_kategorikal.head(10)

# Membentuk data berisi kolom-kolom numerikal (data yang bertipe float64 dan int64)
kolom_numerikal = data[data.columns[(data.dtypes == "float64") | (data.dtypes == "int64")]]

# Menampilkan data kolom numerikal
kolom_numerikal.head(10)

"""## A. Analisis Kolom `explicit`"""

# Membentuk DataFrame pada kolom explicit
explicit = pd.DataFrame(data["explicit"])

# Mendapatkan nilai-nilai yang berbeda pada kolom explicit beserta jumlahnya
nilai_unik, jumlah_nilai = np.unique(explicit, return_counts = True)

# Membentuk plot
fig, ax = plt.subplots(figsize = (6, 6))

# Memisahkan salah satu bagian pada pie plot
true_part = [0, 0.1]
colors = sns.color_palette("pastel")

# Membentuk pie plot
ax.pie(jumlah_nilai, labels = nilai_unik, autopct = "%1.2f%%",
       startangle = 90, colors = colors, explode = true_part)
ax.axis("equal")

# Memberikan judul pada plot
ax.set_title("Distribusi Lagu Berlirik Eksplisit")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, hanya 8.55% dari seluruh lagu memiliki lirik yang bersifat explisit.

## B. Analisis Distribusi Kolom Numerikal dengan Histogram
"""

sns.set_style("darkgrid")
sns.set(rc = {"axes.facecolor" : "lightyellow", "figure.facecolor" : "white"})
kolom_numerikal.hist(figsize = (20, 20), bins = 20, xlabelsize = 10, ylabelsize = 10)
plt.tight_layout(rect = [0, 0.05, 1, 0.95])
plt.suptitle("Histogram dari Kolom Numerikal", fontsize = 20)
plt.ylabel("Jumlah")
plt.show()

"""Gambar di atas dapat diinterpretasikan sebagai berikut.
* Kolom `danceability`, `valence`, dan `tempo` mendekati distribusi normal. Kolom `popularity` juga mendekati distribusi normal, namun mayoritas data bernilai 0.
* Kolom `loudness` memiliki histogram yang bersifat left-skewed. Artinya mayoritas data bernilai tinggi, yang berarti banyak musik memiliki `loudness` sekitar -15 hingga 0 dB.
* Kolom `speechiness`, `acousticness`, dan `liveness` memiliki histogram yang bersifat right-skewed. Artinya mayoritas data pada kolom-kolom tersebut bernilai rendah.
* Kolom `energy` memiliki distribusi yang semakin tinggi untuk tingkat energi yang semakin tinggi.
* Kolom `duration_ms` menunjukkan mayoritas lagu memiliki durasi dibawah 1000000 milidetik.
* Kolom `mode` hanya memiliki 2 nilai data, yaitu 0 dan 1, sesuai dengan arti dari `mode`. Nilai 1 lebih banyak dari 0 yang menunjukkan mayoritas lagu menggunakan skala mayor.
* Kolom `instrumentalness` memiliki nilai mayoritas mendekati yang berarti mayoritas lagu bukan merupakan instrumental (hanya berisi iringan musik tanpa lirik).

## C. Korelasi Seluruh Variabel Numerik dengan Heatmap

Sebelum melihat korelasi dari seluruh variabel numerik, akan ditetapkan batasan nilai korelasi beserta artinya. Misalkan $x$ merupakan nilai korelasi suatu variabel
* Korelasi bernilai $0.00 \leq x \leq 0.30$ dan $-0.30 \leq x \leq 0.00$ merupakan korelasi yang bersifat sangat lemah. Artinya, variabel-variabel tersebut memiliki keterkaitan yang kecil atau bahkan tidak ada kaitan.
* Korelasi bernilai $0.31 \leq x \leq 0.60$ dan $-0.60 \leq x \leq -0.31$ merupakan korelasi yang bersifat cukup kuat. Artinya, variabel-variabel tersebut memiliki keterkaitan yang cukup kuat satu sama lain.
* Korelasi bernilai $0.61 \leq x \leq 1.00$ dan $-1.00 \leq x \leq -0.61$ merupakan korelasi yang bersifat sangat kuat. Artinya, variabel-variabel tersebut memiliki keterkaitan yang kuat atau bahkan sangat kuat.

Berdasarkan 3 tingkatan tersebut, korelasi dibagi menjadi 2, yaitu korelasi positif dan korelasi negatif.
* Korelasi positif merupakan korelasi yang bernilai $0.00 <x \leq 1.00$. Artinya, semakin tinggi nilai salah satu variabel, maka nilai variabel lainnya juga akan semakin tinggi. Hal ini berlaku sebaliknya.
* Korelasi positif merupakan korelasi yang bernilai $-1.00 <x \leq 0.00$. Artinya, semakin tinggi nilai salah satu variabel, maka nilai variabel lainnya justru akan semakin rendah. Hal ini berlaku sebaliknya.
"""

# Mencari korelasi antara masing-masing variabel numerik dengan korelasi pearson
corr = data.corr(method = "pearson", numeric_only = True)

# Membentuk heatmap antara masing-masing variabel numerik dan ditampilkan dalam bentuk desimal 2 angka di belakang koma
plt.figure(figsize = (10, 10))
sns.heatmap(corr, annot = True, fmt = ".2f", annot_kws = {"size": 8})

# Menambahkan judul pada plot
plt.title("Heatmap dari Korelasi Antara Masing-Masing Variabel Numerik")

# Menampilkan plot
plt.show()

"""Heatmap di atas dapat diinterpretasikan sebagai berikut.
* Variabel `danceability` berkorelasi positif yang cukup kuat terhadap variabel `valence`
* Variabel `energy` berkorelasi positif yang kuat terhadap variabel `loudness`, namun berkorelasi negatif yang kuat terhadap variabel `acousticness`
* Variabel `loudness` berkorelasi negatif yang cukup kuat terhadap variabel `acousticness` dan variabel `instrumentalness`
* Variabel `instrumentalness` berkorelasi negatif yang cukup kuat terhadap variabel `valence`

Selain yang disebutkan di atas, seluruh variabel memiliki korelasi yang lemah antara satu dengan yang lain.

## D. Scatter Plot Antara Variabel `danceability` dengan `valence`
"""

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk scatter plot dengan garis trendline
sns.scatterplot(data = kolom_numerikal, x = "danceability", y = "valence")
sns.regplot(data = kolom_numerikal, x = "danceability",
            y = "valence", scatter = False, color = "red")

# Menambahkan judul pada plot
plt.title("Scatter Plot Antara Variabel danceability dengan valence")

# Menampilkan plot
plt.show()

"""* Terlihat bahwa variabel `danceability` berkorelasi positif yang cukup kuat terhadap variabel `valence`, terlihat dari garis yang mengarah ke atas kanan.
* Kedua variabel ini berkorelasi positif cukup kuat karena lagu yang memiliki perasaan positif seperti senang tentu juga cocok untuk menari.
* Akan aneh apabila lagu sedih bisa digunakan untuk menari, sehingga dapat dilihat bahwa lagu yang yang memang memiliki perasaan negatif seperti sedih dan marah tidak cocok untuk menari.

## E. Scatter Plot Antara Variabel `energy` dengan `loudness` dan `acousticness`
"""

# Membentuk plot dengan subplot sejumlah 4 berukuran 2 x 2
fig, axes = plt.subplots(1, 2, figsize = (10, 5))

# Mengubah array multi dimensi menjadi array 1 dimensi
axes = axes.flatten()

# Membentuk dictionary dari variabel yang memiliki nilai korelasi lebih dari / sama dengan 0.2
data_x = {0: "loudness", 1: "acousticness"}

# Mendeskripsikan kolom-kolom numerikal yang akan digunakan berdasarkan dictionary di atas
deskripsi_kolom = ["loudness", "acousticness"]

# Membentuk plot scatter untuk masing-masing kolom beserta garis trend
for keys, values in data_x.items():
    sns.scatterplot(data = data, x = values, y = "energy", ax = axes[keys])
    sns.regplot(data = data, x = values, y = "energy",
                scatter = False, ax = axes[keys], color = "red")

    # Menambahkan judul untuk masing-masing plot
    judul = "\n".join(textwrap.wrap(f"Plot Scatter dari energy Terhadap {deskripsi_kolom[keys]}", width = 50))
    axes[keys].set_title(judul)
    axes[keys].title.set_size(12)

# Mengatur susunan agar tidak berhimpitan
plt.tight_layout()

# Menampilkan plot
plt.show()

"""* Terlihat bahwa variabel `energy` berkorelasi positif yang kuat terhadap variabel `loudness`, terlihat dari garis yang mengarah ke atas kanan, tetapi berkorelasi negatif yang cukup kuat terhadap variabel `acousticness`, terlihat dari garis yang mengarah ke bawah kanan.
* Secara umum, semakin keras suara lagu tersebut, semakin berenergi lagu tersebut, terutama pada genre seperti metal music. Oleh karena itu, variabel `energy` dan `loudness` berkorelasi positif yang kuat.
* Sementara itu, lagu akustik biasanya menggunakan alat musik akustik yang tentu suaranya lebih pelan dibanding alat musik elektrik, serta lagu akustik biasa dinyanyikan dengan suara yang pelan, indah, dan tanpa batuan mikrofon. Akibatnya, jika lagu tersebut merupakan akustik, tentu energinya lebih rendah dibanding lagu non akustik. Oleh karena itu, variabel `energy` dan `acousticness` berkorelasi negatif yang cukup kuat.

## F. Scatter Plot antara Variabel `loudness` dengan `acousticness` dan `instrumentalness`
"""

# Membentuk plot dengan subplot sejumlah 4 berukuran 2 x 2
fig, axes = plt.subplots(1, 2, figsize = (10, 5))

# Mengubah array multi dimensi menjadi array 1 dimensi
axes = axes.flatten()

# Membentuk dictionary dari variabel yang memiliki nilai korelasi lebih dari / sama dengan 0.2
data_x = {0: "acousticness", 1: "instrumentalness"}

# Mendeskripsikan kolom-kolom numerikal yang akan digunakan berdasarkan dictionary di atas
deskripsi_kolom = ["acousticness", "instrumentalness"]

# Membentuk plot scatter untuk masing-masing kolom beserta garis trend
for keys, values in data_x.items():
    sns.scatterplot(data = data, x = values, y = "loudness", ax = axes[keys])
    sns.regplot(data = data, x = values, y = "loudness",
                scatter = False, ax = axes[keys], color = "red")

    # Menambahkan judul untuk masing-masing plot
    judul = "\n".join(textwrap.wrap(f"Plot Scatter dari loudness Terhadap {deskripsi_kolom[keys]}", width = 50))
    axes[keys].set_title(judul)
    axes[keys].title.set_size(12)

# Mengatur susunan agar tidak berhimpitan
plt.tight_layout()

# Menampilkan plot
plt.show()

"""* Terlihat bahwa variabel `loudness` berkorelasi negatif yang cukup kuat terhadap variabel `acousticness` dan `instrumentalness`, terlihat dari garis yang mengarah ke bawah kanan.
* Seperti pada pembahasan sebelumnya, lagu akustik cenderung memiliki suara yang pelan dan indah sehingga suaranya tidak kencang.
* Selain itu, musik yang hanya instrumental (hanya iringan alat musik tanpa lirik) cenderung memiliki suara konstan yang cukup kencang dibandingkan dengan musik non instrumental yang iringan musiknya akan sedikit pelan ketika lirik lagu dinyanyikan.

## G. Scatter Plot antara Variabel `instrumentalness` dengan `valence`
"""

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk scatter plot antara kolom instrumentalness dengan valence
sns.scatterplot(data = kolom_numerikal, x = "instrumentalness", y = "valence")

# Membentuk garis trend untuk melihat korelasi
sns.regplot(data = kolom_numerikal, x = "instrumentalness",
            y = "valence", scatter = False, color = "red")

# Memberikan judul pada plot
plt.title("Scatter Plot Antara Variabel instrumentalness dengan valence")

# Menampilkan plot
plt.show()

"""* Terlihat bahwa variabel `instrumentalness` berkorelasi negatif yang cukup kuat terhadap variabel `valence`, terlihat dari garis yang mengarah ke bawah kanan.
* Biasanya, suasana ceria dalam lagu dibawakan bersamaan dengan nyanyian lirik lagu. Sementara suasana negatif, terutama sedih, dibawakan hanya dalam bentuk instrumental (contohnya dengan violin saja)

## H. Top 10 Album dengan Jumlah Musik Terbanyak
"""

# Mengatur style warna pada seaborn
sns.set_style("darkgrid")
sns.set(rc = {"axes.facecolor" : "lightyellow", "figure.facecolor" : "white"})

# Mencari top 10 album yang memiliki jumlah lagu terbanyak
top_albums = data["album_name"].value_counts().head(10).reset_index()
top_albums.columns = ["album_name", "frequency"]

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom album_name dengan frequency
sns.barplot(x = "frequency", y = "album_name", data = top_albums,
            palette = "seismic", zorder = 3, width = 0.5, hue = "album_name")

# Memberi judul dan label pada plot
plt.title(f"Top 10 Album dengan Jumlah Lagu terbanyak")
plt.xlabel("Jumlah Lagu")
plt.ylabel("Album")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, album `Alternative Christmas 2022` merupakan album yang memiliki jumlah lagu terbanyak, hingga mendekati 200 lagu.

## I. Analisis Genre Musik

Sebelumnya, akan dicari jumlah genre yang terdapat dalam data ini.
"""

# Menghitung jumlah genres yang ada
unique_genres = data["track_genre"].unique()
print(len(unique_genres))

"""Hasilnya, terdapat 114 genre musik yang terdapat di data.

### 1. Top 10 Genre Musik Berdasarkan Rata-Rata Popularitas Tertinggi

Selanjutnya, akan dicari 10 genre dengan rata-rata popularitas tertinggi.
"""

# Mencari rata-rata nilai popularitas dari setiap genre
average_popularity_by_genre = data.groupby("track_genre")["popularity"].mean().reset_index()

# Mengambil 10 genre dengan nilai rata-rata popularitas tertinggi
top10_popular_genre = average_popularity_by_genre.nlargest(10, "popularity")

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom popularity dengan track_genre
sns.barplot(x = "popularity", y = "track_genre", data = top10_popular_genre,
            palette = "seismic", zorder = 3, width = 0.5, hue = "track_genre")

# Memberi judul dan label pada plot
plt.title("Top 10 Genre dengan Rata-Rata Popularitas Tertinggi")
plt.xlabel("Skor Rata-Rata Popularitas")
plt.ylabel("Genre")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, genre pop-film merupakan genre yang memiliki popularitas tertinggi secara rata-rata dibandingkan dengan genre lainnya, mendekati skor 60.

### 2. Top 10 Genre Musik yang Memiliki Lirik Eksplisit
"""

# Mencari rata-rata tingkat eksplisitas lirik dari setiap genre
explicit_ratio_by_genre = data.groupby("track_genre")["explicit"].mean().reset_index()

# Mengambil 10 genre dengan nilai rata-rata tingkat eksplisitas lirik tertinggi
top10_explicit_genres = explicit_ratio_by_genre.nlargest(10, "explicit")

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom popularity dengan track_genre
sns.barplot(x = "explicit", y = "track_genre", data = top10_explicit_genres,
            palette = "seismic", zorder = 3, width = 0.5, hue = "track_genre")

# Memberi judul dan label pada plot
plt.title("Top 10 Genre dengan Rasio Rata-Rata Eksplisit Tertinggi")
plt.xlabel("Rasio Explisit")
plt.ylabel("Genre")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, genre komedi merupakan genre yang memiliki rasio lirik eksplisit tertinggi dibandingkan genre lainnya dengan rasio sekitar 0.65.

### 3. Genre yang memiliki Top 0.1% Jumlah Lagu Berdasarkan Popularitas
"""

# Mengurutkan data berdasarkan nilai popularitas
data_sorted = data.sort_values(by = "popularity", ascending = False)

# Mengambil 0.1% data
top_01_percent = data_sorted.head(int(0.001 * len(data_sorted)))

# Menghitung jumlah lagu pada setiap genre dari 0.1% data
top_genres_count = top_01_percent.groupby("track_genre").size().reset_index(name = "count")

# Mengurutkan top_genres_count berdasar jumlah lagu pada setiap genre
top_genres_count = top_genres_count.sort_values(by = "count", ascending = False)

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom count dengan track_genre
sns.barplot(x = "count", y = "track_genre", hue = "track_genre",
            data = top_genres_count, palette = "seismic")

# Memberi judul dan label pada plot
plt.title("Jumlah Lagu pada Top 0.1% Berdasarkan Genre")
plt.xlabel("Jumlah Lagu")
plt.ylabel("Genre")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, genre pop memiliki jumlah lagu terbanyak pada top 0.1% lagu dengan jumlah lebih dari 20.

### 4. Top 10 Genre dengan Jumlah Penyanyi Terbanyak
"""

# Menghitung jumlah artis pada setiap genre
total_artist_by_genre = data.groupby("track_genre")["artists"].nunique().reset_index()

# Mengambil 10 genre dengan jumlah artis terbanyak
top10_artist_genres = total_artist_by_genre.nlargest(10, "artists")

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom artists dengan track_genre
sns.barplot(x = "artists", y = "track_genre", data = top10_artist_genres,
            zorder = 3, width = 0.5, hue = "track_genre", palette = "seismic")

# Memberi judul dan label pada plot
plt.title("Top 10 Jumlah Penyanyi Pada Setiap Genre")
plt.xlabel("Jumlah Penyanyi")
plt.ylabel("Genre")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, genre dubstep merupakan genre yang memiliki artis terbanyak, berjumlah lebih dari 700.

## J. Analisis Penyanyi/Artis

Sebelumnya, akan dicari jumlah penyanyi yang terdapat dalam data ini.
"""

# Menghitung jumlah penyanyi yang ada
unique_artist = data["artists"].unique()
print(len(unique_artist))

"""Hasilnya, terdapat 31437 jumlah penyanyi yang terdapat di data.

### 1. Top 10 Penyanyi/Artis yang Memiliki Rata-Rata Popularitas Tertinggi
"""

# Mencari rata-rata nilai popularitas dari setiap penyanyi
average_popularity_by_artist = data.groupby("artists")["popularity"].mean().reset_index()

# Mengambil 10 penyanyi dengan nilai rata-rata popularitas tertinggi
top10_popular_artists = average_popularity_by_artist.nlargest(10, "popularity")

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom popularity dengan artists
sns.barplot(x = "popularity", y = "artists", data = top10_popular_artists,
            palette = "seismic", zorder = 3, width = 0.5, hue = "artists")

# Memberi judul dan label pada plot
plt.title("Top 10 Penyanyi dengan Rata-Rata Popularitas Tertinggi")
plt.xlabel("Skor Rata-Rata Popularitas")
plt.ylabel("Penyanyi")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, Sam Smith dan Kim Petras memiliki nilai popularitas tertinggi dibandingkan penyanyi lainnya.

### 2. Top 10 Penyanyi dengan Musik Terbanyak
"""

# Mencari 10 penyanyi dengan jumlah musik terbanyak
top_artists = data["artists"].value_counts().head(10).reset_index()
top_artists.columns = ["artist", "frequency"]

# Mengatur ukuran plot
plt.figure(figsize = (10, 6))

# Membentuk bar plot antara kolom frequency dengan artists
sns.barplot(x = "frequency", y = "artist", data = top_artists,
            palette = "seismic", zorder = 3, width = 0.5, hue = "artist")

# Memberi judul dan label pada plot
plt.title("Top 10 Penyanyi dengan Jumlah Lagu terbanyak")
plt.xlabel("Jumlah Lagu")
plt.ylabel("Penyanyi")

# Menampilkan plot
plt.show()

"""Dari gambar di atas, The Beatles telah membuat lagu terbanyak dibandingkan penyanyi lainnya, yaitu lebih dari 250.

# 6. Content-Based Filtering

## A. Data Preparation

Untuk content-based filtering, kita akan fokus pada judul lagu beserta genre dari lagu tersebut. Oleh karena itu, kita hanya akan mengambil 4 kolom dari data yang dimiliki.
"""

# Mengonversi data series "track_id" menjadi dalam bentuk list
track_id = data["track_id"].tolist()

# Mengonversi data series "track_name" menjadi dalam bentuk list
track_name = data["track_name"].tolist()

# Mengonversi data series "album_name" menjadi dalam bentuk list
album_name = data["album_name"].tolist()

# Mengonversi data series "track_genre" menjadi dalam bentuk list
track_genre = data["track_genre"].tolist()

# Menampilkan banyak data dari masing-masing list
print(len(track_id))
print(len(track_name))
print(len(album_name))
print(len(track_genre))

"""Selanjutnya, kita akan membuat dictionary dari keempat kolom tersebut."""

# Membuat dictionary untuk data ‘resto_id’, ‘resto_name’, dan ‘cuisine’
content_based_data = pd.DataFrame({
    "track_id": track_id,
    "track_name": track_name,
    "album_name": album_name,
    "track_genre": track_genre
})
content_based_data

"""Lalu kita akan menggunakan TF-IDF pada kolom track_genre."""

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data track_genre
tf.fit(content_based_data["track_genre"])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

"""Setelah mendapat index seluruh genre lagu, akan difit lalu ditransformasikan ke bentuk matriks."""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(content_based_data["track_genre"])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""Setelah dibentuk matriks, dibuat tabel berisi judul lagu beserta genrenya berdasarkan TF-IDF yang telah diinisiasi."""

# Membentuk tabel dari judul lagu beserta genrenya berdasarkan tfidf
pd.DataFrame(
    tfidf_matrix.todense(),
    columns = tf.get_feature_names_out(),
    index = content_based_data.track_name
)

"""## B. Modeling

Untuk menentukan content-based filtering, pada proyek ini digunakan cosine similarity untuk mencari kemiripan antar lagu.
"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Setelah itu, akan dibuat tabel berisi cosine similarity antar lagu."""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa judul lagu
cosine_sim_df = pd.DataFrame(cosine_sim, index = data["track_name"], columns = data["track_name"])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap lagu
cosine_sim_df.sample(10, axis = 1).sample(10, axis = 0)

"""Setelah dibentuk tabel cosine similarity, selanjutnya akan dibuat fungsi untuk menentukan rekomendasi musik berdasarkan content-based filtering.

## C. Pengujian Sistem Rekomendasi
"""

def content_based_music_recommendations(nama_lagu, similarity_data = cosine_sim_df,
                                        items = content_based_data, k = 10):

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy Range(start, stop, step)
    index = similarity_data.loc[:, nama_lagu].to_numpy().argpartition(range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1 : -(k + 2) : -1].flatten()]

    # Drop nama_lagu agar nama lagu yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_lagu, errors = "ignore")

    return pd.DataFrame(closest).merge(items).head(k)

# Menampilkan baris sesuai judul lagu yang ditulis
data[data.track_name.eq('Fire - Killer Hertz Remix')]

"""Setelah fungsi siap digunakan, fungsi dipanggil untuk memberikan rekomendasi musik berdasarkan lagu yang telah dipilih/didengar."""

# Menampilkan rekomendasi lagu berdasarkan lagu yang telah dipilih/didengar
content_based_music_recommendations('Fire - Killer Hertz Remix')

"""# 7. Collaborative-Based Filtering

## A. Data Preparation

Selanjutnya, kita akan menggunakan metode collaborative-based filtering untuk memberikan rekomendasi. Untuk pertama, kita akan melakukan encoding pada track_id agar menjadi angka.
"""

# Mengubah track_id menjadi list tanpa nilai yang sama
track_ids = data["track_id"].unique().tolist()
print("list track_id: ", track_ids)

# Melakukan encoding terhadap track_id
track_to_track_encoded = {x: i for i, x in enumerate(track_ids)}
print("encoded track_id : ", track_to_track_encoded)

# Melakukan proses encoding angka ke track_id
track_encoded_to_track = {i: x for i, x in enumerate(track_ids)}
print("encoded angka ke track_id: ", track_encoded_to_track)

"""Selanjutnya, kita juga melakukan encoding pada track_name agar menjadi angka."""

# Mengubah track_name menjadi list tanpa nilai yang sama
track_name = data["track_name"].unique().tolist()

# Melakukan encoding terhadap track_name
name_to_name_encoded = {x: i for i, x in enumerate(track_name)}

# Melakukan proses encoding angka ke track_name
name_encoded_to_name = {i: x for i, x in enumerate(track_name)}

"""Setelah itu, kedua data yang telah diencoding dimapping ke kolom baru"""

# Mapping track_id ke dataframe track
data["track"] = data["track_id"].map(track_to_track_encoded)

# Mapping track_name ke dataframe name
data["name"] = data["track_name"].map(name_to_name_encoded)

"""Setelah semua dilakukan, kita melihat hasil encoding dan mapping."""

# Mendapatkan jumlah track_id
num_track = len(track_to_track_encoded)
print(num_track)

# Mendapatkan jumlah track_name
num_name = len(name_encoded_to_name)
print(num_name)

# Mengubah popularity ke dalam nilai float
data["popularity"] = data["popularity"].values.astype(np.float32)

# Mencari nilai minimum popularity
min_popularity = min(data["popularity"])

# Mencari nilai maksimal popularity
max_popularity = max(data["popularity"])

print("Number of Track ID: {}, Number of Track Name: {}, Min popularity: {}, Max popularity: {}".format(
    num_track, num_name, min_popularity, max_popularity
))

"""Untuk mendapatkan data yang valid, kita akan mengacak seluruh posisi baris pada data."""

# Mengacak dataset
collaborative_based = data[["track", "name", "popularity"]].sample(frac = 1, random_state = 42)
collaborative_based

"""Setelah data siap digunakan, selanjutnya data dibagi untuk proses pelatihan model, yaitu 80% untuk data training dan 20% untuk data testing."""

# Membuat variabel x untuk mencocokkan data track dan nama menjadi satu value
x = collaborative_based[["track", "name"]].values

# Membuat variabel y untuk membuat popularity dari hasil
y = collaborative_based["popularity"].apply(lambda x: (x - min_popularity) / (max_popularity - min_popularity)).values

# Membagi data menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * data.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""## B. Modeling

Selanjutnya, kita akan membentuk model dengan embedding layer untuk data `track` dan `name`.
"""

class RecommenderNet(tf.keras.Model):

    # Insialisasi fungsi
    def __init__(self, num_track, num_name, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_track = num_track
        self.num_name = num_name
        self.embedding_size = embedding_size

        # Membentuk layer embedding untuk track
        self.track_embedding = layers.Embedding(
            num_track,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )

        # Membentuk layer embedding untuk name
        self.name_embedding = layers.Embedding(
            num_name,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )

        # Membentuk layer embedding untuk name_bias dan track_bias
        self.name_bias = layers.Embedding(num_name, 1)
        self.track_bias = layers.Embedding(num_track, 1)

    def call(self, inputs):
        track_vector = self.track_embedding(inputs[:,0]) # memanggil layer embedding 1
        track_bias = self.track_bias(inputs[:, 0]) # memanggil layer embedding 2
        name_vector = self.name_embedding(inputs[:, 1]) # memanggil layer embedding 3
        name_bias = self.name_bias(inputs[:, 1]) # memanggil layer embedding 4

        dot_track_name = tf.tensordot(track_vector, name_vector, 2)

        x = dot_track_name + track_bias + name_bias

        # Menggunakan fungsi aktivasi sigmoid
        return tf.nn.sigmoid(x)

"""Setelah model dibuat, selanjutnya model akan dicompile dengan loss, optimizer, dan metrik evaluasi bersesuaian."""

# Inisialisasi model
model = RecommenderNet(num_track, num_name, 50)

# Model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate = 0.001),
    metrics = [tf.keras.metrics.RootMeanSquaredError()]
)

"""Setelah persiapan model selesai, model dilatih dengan `epochs` sebanyak 50."""

# Memulai training
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 32,
    epochs = 50,
    validation_data = (x_val, y_val)
)

"""Dari hasil di atas, setelah 50 epochs, model memiliki RMSE untuk training sebesar `0.0303` dan RMSE untuk validation sebesar `0.1892`.

## C. Evaluation

Akan divisualisasikan metrik evaluasi dari hasil training di atas.
"""

# Membuat line plot untuk menunjukkan metrik evaluasi
plt.plot(history.history["root_mean_squared_error"])
plt.plot(history.history["val_root_mean_squared_error"])

# Menambahkan judul, label, dan legend pada plot
plt.title("Metrik Evaluasi pada Model")
plt.ylabel("Root Mean Squared Error (RMSE)")
plt.xlabel("Epoch")
plt.legend(["Training", "Validation"], loc = "upper right")

# Menampilkan plot
plt.show()

"""Dengan RMSE untuk training sebesar `0.0303` dan RMSE untuk validation sebesar `0.1892`, model sudah bagus untuk digunakan sebagai sistem rekomendasi. Selanjutnya akan dibuat fungsi untuk menentukan rekomendasi musik berdasarkan colaborative-based filtering.

## D. Pengujian Sistem Rekomendasi
"""

def recommend_tracks_based_on_track_name(track_name, top_n = 10):
    # Memeriksa apakah nama track ada di dalam mapping nama
    if track_name not in name_to_name_encoded:
        print(f"Track dengan judul '{track_name}' tidak ditemukan.")
        return

    # Encoding nama track sesuai dengan nilai encodingnya
    track_name_encoded = name_to_name_encoded[track_name]

    # Membuat list seluruh ID track yang ada
    all_track_ids = list(track_to_track_encoded.values())

    # Mempersiapkan ID dan nama track untuk prediksi
    track_name_array = np.array([[track_name_encoded]] * len(all_track_ids))
    track_id_array = np.array(all_track_ids).reshape(-1, 1)

    # Membentuk array ID dan nama track untuk prediksi
    track_name_track_id_array = np.hstack((track_id_array, track_name_array))

    # Memprediksi popularitas berdasarkan nama track yang dipilih
    popularity = model.predict(track_name_track_id_array).flatten()

    # Mendapatkan Top-N rekomendasi
    top_popularity_indices = popularity.argsort()[-top_n:][::-1]
    recommended_encoded_track_ids = [all_track_ids[x] for x in top_popularity_indices]

    # Mapping ID track yang sudah di encoding ke dataset awal
    recommended_track_ids = [track_encoded_to_track.get(track_id) for track_id in recommended_encoded_track_ids]

    # Menampilkan Top-N rekomendasi berdasarkan nama track
    print(f"Rekomendasi berdasarkan track dengan judul: '{track_name}'")
    print("10 Rekomendasi Terbaik:")
    for track_id in recommended_track_ids:
        if track_id is not None:
            # Output the actual track name
            track_info = data[data["track_id"] == track_id]
            if not track_info.empty:
                print(f"ID Track: {track_id}, Judul Track: {track_info['track_name'].values[0]}")
            else:
                print(f"ID Track '{track_id}' tidak ada di dalam dataset.")

# Menampilkan baris sesuai judul lagu yang ditulis
data[data.track_name.eq('Fire - Killer Hertz Remix')]

"""Setelah fungsi siap digunakan, fungsi dipanggil untuk memberikan rekomendasi musik berdasarkan lagu yang telah dipilih/didengar."""

# Memanggil fungsi untuk mendapatkan top 10 rekomendasi
recommend_tracks_based_on_track_name("Fire - Killer Hertz Remix", top_n=10)