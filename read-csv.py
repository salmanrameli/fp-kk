import csv
import random
import math

rownum = 0
colnum = 0
jumlah_kromosom = 5

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
edge = int(node + (attributes * node))

"""print info"""
print "rownum = " + str(rownum)
print "colnum = " + str(colnum)
print "attributes = " + str(attributes)
print "jumlah node = " + str(node)
print "jumlah edge = " + str(edge)

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

"""inisialisasi list yang berisi banyak list yang nantinya dipakai untuk menyimpan gen kromosom buatan genetic algorithm"""
kromosom = [[] for i in range(0,10)]

"""generate sekumpulan angka random sebagai gen kromosom genetic algorithm"""
for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom[a].append(gen)

x = 0
y = 0
summation = 0
indexa = 1

for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom[x][b]
            summation += hasil

        print "summation " + str(indexa) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        print "aktivasi " + str(indexa) + ": " + str(aktivasi)
        indexa += 1
