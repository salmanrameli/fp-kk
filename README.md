# Penggabungan Algoritma Jaringan Saraf Tiruan dengan Genetic Algorithm
Final project kuliah Kecerdasan Komputasional Teknik Informatika ITS semester gasal tahun ajaran 2016 - 2017

## Detail dataset
- jumlah atribut: 35 (1 atribut sebagai hasil analisa)
- jumlah data: 324

## 
1. hitung jumlah node pada hidden layer
2. generate Y kromosom yang berisi angka random sebaga weight pada JST
3. masukkan elemen setiap kromosom sebagai weight pada JST
4. hitung presentase error tiap kromosom
5. ambil 10% kromosom dengan error terkecil
6. kembang-biakkan 10% kromosom ini sampai kembali berjumlah Y kromosom
7. ulangi sebanyak yang diperlukan

## Hasil Analisa Program
Catatan:
* Program dijalankan pada komputer desktop dengan prosesor Intel Core i7-6700 dan memori DDR4 16Gb
* Hampir bisa dipastikan bahwa error konstan dari iterasi pertama sampai iterasi terakhir

### Selection random & reproduction inversion mutation, 5 hidden node
* iterasi: 10
* Jumlah dataset: 324
* Jumlah kromosom: 100
* Running time: 40.394 detik
* Error: 64%

----------
* iterasi: 20
* Jumlah dataset: 324
* Jumlah kromosom: 100
* Running time:  80.317 detik
* Error: 66%

----------
* iterasi: 30
* Jumlah dataset: 324
* Jumlah kromosom: 100
* Cuma bisa sampai 21 iterasi, setelah itu inisialisasi weight gagal

------------------------------
* iterasi: 10
* Jumlah dataset: 324
* Jumlah kromosom: 200
* Running time:  79.471 detik
* Error: 65%

----------
* iterasi: 20
* Jumlah dataset: 324
* Jumlah kromosom: 200
* Running time:  detik
* Cuma bisa sampai 12 iterasi, setelah itu inisialisasi weight gagal

------------------------------
### Selection random & reproduction inversion mutation, 10 hidden node
* iterasi: 10
* Jumlah dataset: 324
* Jumlah kromosom: 100
* Running time:  76.993 detik
* Error: 67%

----------
* iterasi: 20
* Jumlah dataset: 324
* Jumlah kromosom: 100
* Running time:  detik
* Cuma bisa sampai 12 iterasi, setelah itu inisialisasi weight gagal

------------------------------
* iterasi: 10
* Jumlah dataset: 324
* Jumlah kromosom: 200
* Running time:  detik
* Cuma bisa sampai 5 iterasi, setelah itu inisialisasi weight gagal
