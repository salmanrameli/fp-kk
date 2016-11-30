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
node = 5

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
kromosom_input_1 = [[] for i in range(0, jumlah_kromosom)] #   list yang menyimpan weight dari input layer ke hidden layer 1
kromosom_input_2 = [[] for i in range(0, jumlah_kromosom)] #   list yang menyimpan weight dari input layer ke hidden layer 2
kromosom_input_3 = [[] for i in range(0, jumlah_kromosom)] #   list yang menyimpan weight dari input layer ke hidden layer 3
kromosom_input_4 = [[] for i in range(0, jumlah_kromosom)] #   list yang menyimpan weight dari input layer ke hidden layer 4
kromosom_input_5 = [[] for i in range(0, jumlah_kromosom)] #   list yang menyimpan weight dari input layer ke hidden layer 5

hidden_layer_1 = [[] for i in range(0, rownum)] #   list yang menyimpan hasil aktivasi pada node 1 di hidden layer
hidden_layer_2 = [[] for i in range(0, rownum)] #   list yang menyimpan hasil aktivasi pada node 2 di hidden layer
hidden_layer_3 = [[] for i in range(0, rownum)] #   list yang menyimpan hasil aktivasi pada node 3 di hidden layer
hidden_layer_4 = [[] for i in range(0, rownum)] #   list yang menyimpan hasil aktivasi pada node 4 di hidden layer
hidden_layer_5 = [[] for i in range(0, rownum)] #   list yang menyimpan hasil aktivasi pada node 5 di hidden layer

kromosom_hidden_1 = [[] for i in range(0, rownum)]
kromosom_hidden_2 = [[] for i in range(0, rownum)]
kromosom_hidden_3 = [[] for i in range(0, rownum)]
kromosom_hidden_4 = [[] for i in range(0, rownum)]
kromosom_hidden_5 = [[] for i in range(0, rownum)]

output_layer = [[] for i in range(0, rownum)]

"""generate sekumpulan angka random sebagai gen kromosom genetic algorithm"""
for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom_input_1[a].append(gen) #   berisi 34 angka floating point sebagai weight dari input layer ke node 1

for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom_input_2[a].append(gen) #   berisi 34 angka floating point sebagai weight dari input layer ke node 2

for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom_input_3[a].append(gen) #   berisi 34 angka floating point sebagai weight dari input layer ke node 3

for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom_input_4[a].append(gen) #   berisi 34 angka floating point sebagai weight dari input layer ke node 4

for a in range(jumlah_kromosom): #    index baris
    for b in range(attributes): #    index kolom
        gen = random.uniform(1,10)
        kromosom_input_5[a].append(gen) #   berisi 34 angka floating point sebagai weight dari input layer ke node 5

x = 0
index = 1

'''menghitung summation dan fungsi aktivasi pada hidden layer node 1'''
for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom_input_1[x][b]
            summation += hasil

        #print "summation " + str(index) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        #print "aktivasi " + str(index) + ": " + str(aktivasi)
        index += 1

        hidden_layer_1[a].append(aktivasi)

# for b in range(rownum):
#     print hidden_layer_1[b]

x = 0
index = 1

'''menghitung summation dan fungsi aktivasi pada hidden layer node 2'''
for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom_input_2[x][b]
            summation += hasil

        #print "summation " + str(index) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        #print "aktivasi " + str(index) + ": " + str(aktivasi)
        index += 1

        hidden_layer_2[a].append(aktivasi)

x = 0
index = 1

'''menghitung summation dan fungsi aktivasi pada hidden layer node 3'''
for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom_input_3[x][b]
            summation += hasil

        #print "summation " + str(index) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        #print "aktivasi " + str(index) + ": " + str(aktivasi)
        index += 1

        hidden_layer_3[a].append(aktivasi)

x = 0
index = 1

'''menghitung summation dan fungsi aktivasi pada hidden layer node 4'''
for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom_input_4[x][b]
            summation += hasil

        #print "summation " + str(index) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        #print "aktivasi " + str(index) + ": " + str(aktivasi)
        index += 1

        hidden_layer_4[a].append(aktivasi)

x = 0
index = 1

'''menghitung summation dan fungsi aktivasi pada hidden layer node 5'''
for x in range(jumlah_kromosom):
    for a in range(rownum):
        for b in range(attributes):
            summation = 0
            hasil = float(matrix[a][b]) * kromosom_input_5[x][b]
            summation += hasil

        #print "summation " + str(index) + ": " + str(summation)
        aktivasi = 1 / (1 + math.exp(-1 * summation))

        #print "aktivasi " + str(index) + ": " + str(aktivasi)
        index += 1

        hidden_layer_5[a].append(aktivasi)
