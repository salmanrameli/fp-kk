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

