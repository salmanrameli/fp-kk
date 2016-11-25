# Penggabungan Algoritma Jaringan Saraf Tiruan dengan Genetic Algorithm
final project kuliah kecerdasan komputasional

##detail dataset
- jumlah atribut: 35 (1 atribut sebagai hasil analisa)
- jumlah data: 324

##prosedur
1. hitung jumlah node pada hidden layer
2. generate Y kromosom yang berisi angka random sebaga weight pada JST
3. masukkan elemen setiap kromosom sebagai weight pada JST
4. hitung presentase error tiap kromosom
5. ambil 10% kromosom dengan error terkecil
6. kembang-biakkan 10% kromosom ini sampai kembali berjumlah Y kromosom
7. ulangi sebanyak yang diperlukan

##progress
- [x] normalisasi dataset
- [x] masukkan dataset pada list
- [x] baca jumlah baris dan kolom dataset
- [x] hitung jumlah node pada hidden layer
- [x] hitung jumlah edge yang akan digunakan pada JST
- [x] buat list yang berisi list kosong sebanyak jumlah kromosom genetic algorithm
- [x] generate angka desimal random sebagai elemen kromosom yang nantinya dipakai sebagai weight JST
- [x] append angka desimal yang sudah dibuat ke list
- [ ] hitung summation input layer dengan hidden layer
- [ ] hitung fungsi aktivasi tiap hidden layer
- [ ] hitung summation hidden layer dengan output layer
- [ ] hitung fungsi aktivasi output layer
- [ ] hitung error hasil output layer dengan jawaban pada dataset
- [ ] hitung MSE dari setiap kromosom
- [ ] ambil 10 kromosom dengan error terkecil
- [ ] kosongkan list 90 kromosom yang tidak dipilih
- [ ] kembang-biakkan 10 kromosom yang diambil sehingga kembali berjumlah 100
