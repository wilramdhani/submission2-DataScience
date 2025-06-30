#### Setup Environment

Untuk memastikan proyek ini dapat dijalankan dengan lancar, ikuti langkah-langkah berikut untuk menyiapkan lingkungan pengembangan:

1.  **Kloning Repository (Opsional):** Jika kode proyek tersedia di repository (misalnya, GitHub), kloning repository tersebut ke mesin lokal Anda:

    ```bash
    git clone [URL REPOSITORY]
    cd [NAMA REPOSITORY]
    ```

2.  **Membuat dan Mengaktifkan Virtual Environment (venv):**

    - Buat virtual environment untuk mengisolasi dependensi proyek:
      ```bash
      python -m venv venv
      ```
    - Aktifkan virtual environment:
      - **Untuk Windows:**
        ```bash
        venv\Scripts\activate
        ```
      - **Untuk macOS dan Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Instal Dependensi:** Setelah virtual environment diaktifkan, instal dependensi proyek menggunakan `pip`:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Unduh Dataset:** Pastikan Anda telah mengunduh dataset dari tautan yang diberikan dan menempatkannya di direktori yang sesuai. (Misalnya, direktori `data/`)

#### Data Preparation

Pada proses persiapan data meliputi beberapa tahap yaitu sebagai berikut:

1. Memeriksa dengan melihat apakah ada anomali atau penyimpangan pada dataset yang dimiliki
2. Memeriksa distribusi kolom target untuk nantinya dilihat apakah akan dilakukan balancing data atau tidak (pada akhirnya dicase ini kita harus melakukan balancing data target karna data target terindikasi imbalanced) .
3. Mengubah kolom target menjadi data numerikal dengan menggunakan `LabelEncoder`.
4. Mmembuat grafik heatmap korelasi untuk melihat hubungan fitur-fitur pada kolom target.
5. Memilih kolom-kolom atau fitur yang memiliki korelasi yang cukup dengan kolom target.
6. Memisahkan data menjadi 2 bagian yaitu data training dan data testing dengan perbandingan 80% data training dan 20% data testing dan melakukan scaling pada fitur.
7. Melakukan balancing data pada kolom target karena target terindikasi imbalanced sehingga harus diseimbangkan.

### Modeling

Beberapa model machine learning yang dilatih untuk memprediksi Dropout, Enrolled, & Graduate adalah sebagai berikut:

- **Logistik Regression**: untuk memahami kemungkinan mahasiswa dropout, enrolled atau graduate berdasarkan beberapa faktor.
- **Decision Tree Classifier**: untuk menangkap hubungan non-linear antar variabel.
- **SVM**: digunakan untuk memaksimalkan margin antara kelas dropout, enrolled, atau graduate dalam dataset yang memiliki dimensi tinggi.
- **Random Forest Classifier**: metode ensemble untuk prediksi yang lebih akurat dan mengurangi overfitting.
- **Neural Network**: Digunakan untuk menangkap pola kompleks dalam data melalui beberapa lapisan tersembunyi.
  Berdasarkan model model yang dilatih, model Random Forest Classifier memberikan performa yang baik diantara model-model lainnya.
  Model yang dipilih akan digunakan untuk membuat prediksi pada data masa depan.

### Evaluation

Metrik evaluasi model yang digunakan dalam proyek ini meliputi:

- **Accuracy**: Untuk mengukur ketepatan prediksi model secara keseluruhan.
- **Precision & Recall**: Untuk memahami trade-off antara memprediksi positif yang benar dan positif yang salah.
- **F1-Score**: Keseimbangan antara presisi dan recall, terutama berguna dalam menangani ketidakseimbangan kelas.
- **Confusion Matrix**: Untuk memvisualisasikan kinerja dan mengidentifikasi area di mana model dapat salah mengklasifikasikan.
  berikut adalah hasil evaluasi yang didapat pada model machine learning yang telah dilatih
  | Model | Accuracy Training | Accuracy Testing |
  |---------------|--------------|--------------|
  | Logistic Regression | 73.06% | 74.68% |
  | Decision Tree | 100% | 65.87% |
  | SVM | 77.46% | 73.67% |
  | Random Forest | 100% | 75.93% |
  | Random Forest (Hyperparameter Tuning) | 82.17% | 75.36% |
  | Neural Network | 71.75% | 72.31% |

## Business Dashboard

Business dashboard yang telah dibuat menggunakan Looker Studio dengan dashboard yang dibuat adalah dashboard interaktif. Anda dapat melihat dashboard yang telah dibuat dengan klik pada [Link ini](https://lookerstudio.google.com/u/0/reporting/b383483b-7289-4b0a-8c93-e980599033c1/page/9CHFE)

## Menjalankan Sistem Machine Learning

1. Menyiapkan data: Pastikan dataset yang diperlukan berada di folder yang sesuai, atau tambahkan data baru yang ingin Anda prediksi.
2. Running Model: Untuk menjalankan model prediksi, gunakan script Python yang telah disediakan. Contoh untuk melakukan prediksi dengan model Neural Network:
