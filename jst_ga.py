'''
Anggota Kelompok :
1. Muhammad Al Fatih (5114100039)
2. Jeffry Nasri Faruki (5114100039)
3. Anugra Pratama (5114100099)

A. Spesifikasi Program
	a) Dataset: Menggunakan data diagnosa penyakit mesothelioma

'''
#!/usr/bin/python
import random
import csv
import math
import operator
import time

class Kromosom :
	jumlah_gen =0
	def __init__(self):
		self.gens=[]
		self.error=0
		self.id=0
		self.jumlah_gen=0
		
		self.init_jumlah_gen()
		self.random_gens()
		#self.set_gens(inputs)
	def init_jumlah_gen(self):
		global jumlah_atribut
		global jumlah_node_hidden
		global jumlah_node_output
		self.jumlah_gen=(jumlah_atribut*jumlah_node_hidden)+(jumlah_node_hidden*jumlah_node_output)
	def random_gens(self):
		for i in range(0,self.jumlah_gen):
			self.gens.append(random.uniform(0, 1))
	def set_gens(self,inputs):
		for i in range(0,self.jumlah_gen):
			self.gens[i]=inputs[i]
	def print_gen(self):
		for gen in self.gens:
			print(gen)
class Node:
	def __init__(self):
		self.output=0
	def receive_input(self,input):
		self.activation_sigmoid(input)
	def activation_sigmoid(self,x):
		self.output=float( 1 / (1 + math.exp(-1 * x)))
class JST:
	def __init__(self):
		self.input_layer=[]
		self.hidden_layer=[]
		self.output_layer=[]
		self.weight_hidden_layer=[]
		self.weight_output_layer=[]
		
		self.output=0
	def init_input_layer(self,inputs):
		try:
			global jumlah_atribut
			self.input_layer=[]
			for i in range(0,jumlah_atribut):
				self.input_layer.append(inputs[i])
		except:	
			print("Inisialisasi Input Layer GAGAL")
	def init_hidden_layer(self):
		try:
			global jumlah_node_hidden
			for i in range(0,jumlah_node_hidden):
				self.hidden_layer.append(Node())
			print("Inisialisasi Hidden Layer SUKSES")
		except:	
			print("Inisialisasi Hidden Layer GAGAL")
	def init_output_layer(self):
		try:
			global jumlah_node_output
			for i in range(0,jumlah_node_output):
				self.output_layer.append(Node())
			print("Inisialisasi Output Layer SUKSES")
		except:	
			print("Inisialisasi Output Layer GAGAL")
	def init_weight(self,kromosom):
		try:
			global jumlah_node_hidden
			global jumlah_node_output
			global jumlah_atribut
			for i in range(0,len(kromosom.gens)):
				if(i<(jumlah_atribut*jumlah_node_hidden)):
					self.weight_hidden_layer.append(kromosom.gens[i])
				else:			
					self.weight_output_layer.append(kromosom.gens[i])
			#print("Inisialisasi Weight SUKSES")
		except:	
			print("Inisialisasi Weight GAGAL")
	def calculation_hidden_layer(self):
		#print (self.input_layer)
		iterator=0
		for node_hidden in self.hidden_layer:
			summation=0
			for i in range(0,len(self.input_layer)):
				summation=summation+(float(self.input_layer[i])*float(self.weight_hidden_layer[iterator]))
				iterator=iterator+1
			node_hidden.receive_input(float(summation))
	def calculation_output_layer(self):
		iterator=0
		for node_output in self.output_layer:
			summation=0
			for i in range(0,len(self.hidden_layer)):
				summation=summation+(float(self.hidden_layer[i].output)*float(self.weight_output_layer[iterator]))
				iterator=iterator+1
			node_output.receive_input(float(summation))
			self.output=float(node_output.output)
	def inisialitation(self):
		self.init_hidden_layer()
		self.init_output_layer()
	def process(self,inputs,kromosoms,index_kromosoms):
		#print(inputs)
		self.init_input_layer(inputs)
		self.init_weight(kromosoms[index_kromosoms])
		
		self.calculation_hidden_layer()
		self.calculation_output_layer()
		return self.output
		
def print_kromosoms(kromosoms):			
	for kromosom in kromosoms:
		kromosom().print_gen()
		
#Fungsi Mengitung Rata2
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
	
#Fungsi Inisialisasi Input(Baca file->disimpan di inputs)
def init_inputs():
	global inputs
	global jumlah_atribut
	
	# Baca CSV file , kemudian dimasukkan ke var inputs yg berbrntuk matriks 2d
	f = open('mesothelioma-normalisasi-csv.csv')
	csv_f = csv.reader(f)
	inputs=list(csv_f)
	
	# Hitung Jumlah Atribut
	for input in inputs:
		jumlah_atribut=len(input) - 1

#Fungsi Inisialisasi Kromosom(Memasukkan kromosom ke dalam list kromosoms)		
def init_kromosoms():
	global kromosoms
	global jumlah_kromosom
	global database_gens
	for i in range(0,jumlah_kromosom):
		kromosoms.append(Kromosom())
		kromosoms[-1].set_gens(database_gens[i])


def init_database_gens():
	global database_gens
	
	# Baca CSV file , kemudian dimasukkan ke var database_gens yg berbrntuk matriks 2d
	f = open('database_gens.csv')
	csv_f = csv.reader(f)
	database_gens=list(csv_f)

#Fungsi Inisialisasi JST
def init_jst():
	global jst
	jst.inisialitation()

#Algoritma seleksi metode rank
def selection_rank():
	'''
	Algortima - >
	Seleksi dilakukan dengan cara :
	1. Ranking individu berdasarkan errornya
	2. Pilih individu dengan n ranking teratas (dlm program ini n = 20% dr jumlah kromosom)
	3. individu yg tidak terpilih dihapus
	
	Ket : Individu dalam program ini adalah kromosom
	'''	

	global kromosoms
	n=0.2
	jumlah_parent=int(n*len(kromosoms))
	kromosoms.sort(key=lambda x: x.error)
	for i in range(jumlah_parent,len(kromosoms)):
		del kromosoms[-1]	
#Algoritma seleksi metode random
def selection_random():
	'''
	Algortima - >
	Seleksi dilakukan dengan cara :
	1. Random sebuah angka, disimpan dalam variabel i
	2. Pilih kromosom ke-i menjadi parent
	
	'''	

	global kromosoms
	i=random.randint(0, (len(kromosoms)-1))
	parent=kromosoms[i]
	for i in range(len(kromosoms)):
		del kromosoms[-1]	
	
	kromosoms.append(parent)

#Algoritma seleksi metode tournament		
def selection_tournament():
	'''
	Algortima - >
	Seleksi dilakukan dengan cara :
	1. Pilih individu ke i sebanyak n dalam dalam populasi
		(i dan n adalah bilangan random)
	2. n individu terpilih, selnjutnya dipilih 1 individu terbaik berdasarkan error
	3. individu yg tidak terpilih dihapus
	
	Ket : 	Individu dalam program ini adalah kromosom
			Populasi adalah daftar kromosom
	'''	
	global kromosoms
	n=random.randint(1, len(kromosoms))
	i=0
	kromosom_terpilih=[]
	
	for a in range(n):
		i=random.randint(0, (len(kromosoms)-1))
		kromosom_terpilih.append(kromosoms[i])
	kromosom_terpilih.sort(key=lambda x: x.error)
	
	for i in range(len(kromosoms)):
		del kromosoms[-1]
	
	kromosoms.append(kromosom_terpilih[0])

#Algoritma reproduksi metode mutasi boundary
def reproduction_boundary_mutation():
	global kromosoms
	global jumlah_kromosom
	jumlah_parent=len(kromosoms)
	jumlah_replika=jumlah_kromosom-jumlah_parent
	index_copy=0
	
	for i in range(jumlah_replika):
		if (index_copy>(jumlah_parent-1)):
			index_copy=0
		kromosoms.append(Kromosom())
		for j in range(kromosoms[index_copy].jumlah_gen):
			#print kromosoms[-1].gens[i]
			kromosoms[-1].gens[j] = kromosoms[index_copy].gens[j]
		kromosoms[-1].error = kromosoms[index_copy].error
		
		index_random_gens=random.randint(0, (kromosoms[i+jumlah_parent].jumlah_gen-1))
		kromosoms[i+jumlah_parent].gens[index_random_gens]=random.uniform(0,1)
		index_copy=index_copy+1

#Algoritma reproduksi metode mutasi swap		
def reproduction_swap_mutation():
	global kromosoms
	global jumlah_kromosom
	jumlah_parent=len(kromosoms)
	jumlah_replika=jumlah_kromosom-jumlah_parent
	index_copy=0
	
	for i in range(jumlah_replika):
		if (index_copy>(jumlah_parent-1)):
			index_copy=0
		kromosoms.append(Kromosom())
		
		for j in range(kromosoms[index_copy].jumlah_gen):
			#print kromosoms[-1].gens[i]
			kromosoms[-1].gens[j] = kromosoms[index_copy].gens[j]
		kromosoms[-1].error = kromosoms[index_copy].error
		
		index_random_gens1=random.randint(0, (kromosoms[i+jumlah_parent].jumlah_gen-1))
		index_random_gens2=random.randint(0, (kromosoms[i+jumlah_parent].jumlah_gen-1))
		
		temp=kromosoms[i+jumlah_parent].gens[index_random_gens1]
		kromosoms[i+jumlah_parent].gens[index_random_gens1]=kromosoms[i+jumlah_parent].gens[index_random_gens1]
		kromosoms[i+jumlah_parent].gens[index_random_gens2]=temp
		
		index_copy=index_copy+1

#Algoritma reproduksi metode mutasi inversi		
def reproduction_inversion_mutation():
	global kromosoms
	global jumlah_kromosom
	jumlah_parent=len(kromosoms)
	jumlah_replika=jumlah_kromosom-jumlah_parent
	index_copy=0
	
	for i in range(jumlah_replika):
		if (index_copy>(jumlah_parent-1)):
			index_copy=0
		kromosoms.append(Kromosom())
		
		#Mencopy Gen child dari gen parent
		for j in range(kromosoms[index_copy].jumlah_gen):
			#print kromosoms[-1].gens[i]
			kromosoms[-1].gens[j] = kromosoms[index_copy].gens[j]
		kromosoms[-1].error = kromosoms[index_copy].error
	
		index_random_gens1=random.randint(0, (kromosoms[i+jumlah_parent].jumlah_gen-1))
		index_random_gens2=random.randint(0, (kromosoms[i+jumlah_parent].jumlah_gen-1))
		if(index_random_gens1>index_random_gens2):
			start=index_random_gens2
			stop=index_random_gens1
		else:
			start=index_random_gens1
			stop=index_random_gens2
		
		temp_gens=[]		
		for index in range (start,stop,1):
			temp_gens.append(kromosoms[i+jumlah_parent].gens[index])
		for index in range (start,stop,1):
			kromosoms[i+jumlah_parent].gens[index]=temp_gens[stop-index-1]
		index_copy=index_copy+1

#Main proses algoritma GA		
def ga_process():
	global kromosoms
	
	#selection_tournament()
	#selection_rank()
	selection_random()
	
	#reproduction_boundary_mutation()
	#reproduction_swap_mutation()
	reproduction_inversion_mutation()
	

#Fungsi main Inisialisais
def inisialitation():
	init_database_gens()
	init_inputs()
	init_kromosoms()
	init_jst()	

#Fungsi Main proses 	
def process():
	global kromosoms
	global jumlah_data_belajar
	global jst
	global inputs
	global iterasi_ga_jst
	tresshold=0
	kelas=[]
	kelas_sebenarnya=[]
		
	start = time.time()
	for a in range(0,iterasi_ga_jst):
		# Proses JST -> hitung output -> hitung error tiap kromosom
		###print("Iterasi-ke "+str(a+1))
		for i in range(0,len(kromosoms)):
			outputs=[]
			kelas=[]
			error_kelas=0
			for j in range(0,jumlah_data_belajar):
				outputs.append(jst.process(inputs[j],kromosoms,i))
			tresshold	= mean(outputs)
			for output in outputs:
				if (output<tresshold):
					kelas.append(0.5)
				else:
					kelas.append(1)
			for k in range(0,len(inputs)):
				kelas_sebenarnya.append(inputs[k][-1])
			for l in range(0,len(kelas)):
				if(float(kelas[l])!=float(kelas_sebenarnya[l])):
					error_kelas=error_kelas+1
			kromosoms[i].error=float(error_kelas*100/len(kelas))	
	
		#Proses GA ->Seleksi dan replikasi
		ga_process()
		
		###for kromosom in kromosoms:
		###	print kromosom.gens
		###	print(kromosom.error)
		###print(kromosoms[0].gens)
		###print(kromosoms[0].error)
	
	global output_program
	output_program.write("Hasil= " + str(kromosoms[0].gens) + "\n")
	output_program.write("Error= " + str(kromosoms[0].error)+ "% \n")
	end = time.time()
	if((end-start)>=60):
		output_program.write("Waktu Eksekusi = " + str(int(end)/int(start)) + " menit " +str((end-start)%60) + " detik"+ "\n")

	else:
		output_program.write("Waktu Eksekusi = " + str(end - start) + " detik"+ "\n")
	
if __name__=='__main__':
	output_program= open('output_program.txt',"w+")
	
	iterasi_ga_jst=10
	jumlah_atribut=0
	jumlah_data_belajar=100
	jumlah_kromosom=jumlah_data_belajar
	
	inputs=[]
	inputs.append([])
	kromosoms=[]
	jst=JST()
	
	database_gens=[]
	database_gens.append([])
	#Atribut JST
	jumlah_node_hidden=5
	jumlah_node_output=1
	

	inisialitation()
	process()
	output_program.close()