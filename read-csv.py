import csv
import random

rownum = 0
colnum = 0

"""buka file csv untuk menghitung jumlah baris dan kolom total"""
with open('mesothelioma-small.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
        if rownum == 0:
            header = row
            for a in row:
                colnum += 1
        else:
            for col in row:
                colnum += 1
        rownum += 1

"""menghitung jumlah atribut dengan cara membagi jumlah kolom total dengan jumlah baris kemudian dikurangi 1"""
attributes = (colnum / rownum) - 1

"""menghitung jumlah node pada hidden layer"""
#node = round(float(rownum) / (2 * (float(attributes) + 1)))

node = 1

"""menghitung jumlah link yang dibutuhkan antara input layer dengan hidden layer dan hidden layer dengan output layer"""
jumlah_link = int(node + (attributes * node))

"""print info"""
print "rownum = " + str(rownum)
print "colnum = " + str(colnum)
print "attributes = " + str(attributes)
print "jumlah node = " + str(node)
print "jumlah link = " + str(jumlah_link)

"""buka file csv untuk dimasukkan ke dalam list"""
with open('mesothelioma-small.csv', 'rb') as f:
    reader = csv.reader(f)
    matrix = list(reader)

"""print file csv yang barusan dimasukkan ke list"""
'''
b = 1
for a in matrix:
    if b%34 == 0:
        print "\n"
    else:
        #print a
        continue
    b += 1
'''

#print "matrix[0][0] =" + str(matrix[0][0])

"""inisialisasi list yang berisi banyak list yang nantinya dipakai untuk menyimpan gen kromosom buatan genetic algorithm"""
listoflist = [[] for i in range(0,5)]

"""generate sekumpulan angka random sebagai gen kromosom genetic algorithm"""
for a in range(5):
    for b in range(3):
        angka = random.uniform(1,10)
        listoflist[a].append(angka)

"""contoh akses elemen list"""
print listoflist
print listoflist[0]
print listoflist[0][0]
print listoflist[0][1]
