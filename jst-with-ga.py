import os
import string
import sys
import math
import random
from heapq import nsmallest
import csv
import time

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\n',
    quoting = csv.QUOTE_MINIMAL
)

class Jst():
    def __init__(self, num_input_node, num_hidden_node):
        self.num_input_node = num_input_node
        self.num_hidden_node = num_hidden_node
        self.hidden_weight = []
        self.output_weight = []
        self.threshold = 0

        #init hidden weight dan output weight
        for i in range(num_hidden_node):
            input_weight = []
            for j in range(num_input_node):
                input_weight.append(1)
            self.hidden_weight.append(input_weight)
            self.output_weight.append(1)

    def set_weight(self, hidden_weight, output_weight):
        num_weight_list = len(hidden_weight[0])*len(hidden_weight) + len(output_weight)
        total_weight = len(self.hidden_weight[0])*len(self.hidden_weight) + len(self.output_weight)
        if num_weight_list != total_weight:
            print "list not match"
            return 0
        else:
            for i in range(len(hidden_weight)):
                for j in range(len(hidden_weight[i])):
                    self.hidden_weight[i][j] = hidden_weight[i][j]
                self.output_weight[i] = output_weight[i]
            return 1

    def set_threashold(self, threshold):
        self.threshold = threshold
        return 1

    def sum(self, input_node):
        hidden_sum = []
        for i in range(len(self.hidden_weight)):
            temp = 0
            for j in range(len(input_node)):
                temp = temp + input_node[j] * self.hidden_weight[i][j]
            hidden_sum.append(temp)
        return hidden_sum

    def sigmoid(self, sum_result):
        sigmoid_result = []
        for i in range(self.num_hidden_node):
            result = 1 / (1 + math.exp(-sum_result[i]))
            sigmoid_result.append(result)
        return sigmoid_result

    def calculate_output(self, input_node):
        sigmoid_result = self.sigmoid(self.sum(input_node))
        sum_output = 0
        for i in range(self.num_hidden_node):
            sum_output = sum_output + self.output_weight[i]*sigmoid_result[i]

        if sum_output > self.threshold:
            return 1
        else:
            return 2

class Ga():
    def __init__(self, jst, dataset):
        #initiate atribute
        self.jst = jst
        self.dataset = dataset
        self.hidden_population = []
        self.output_population = []
        self.error = []
        self.num_population = 100

        #initiate 100 random population
        for i in range(self.num_population):
            kromosom = []
            for j in range(self.jst.num_hidden_node):
                temp_input_weight = []
                for k in range(self.jst.num_input_node):
                    temp_input_weight.append(random.random()*2-1)
                kromosom.append(temp_input_weight)
            self.hidden_population.append(kromosom)

        for i in range(self.num_population):
            kromosom = []
            for j in range(self.jst.num_hidden_node):
                kromosom.append(random.random()*2-1)
            self.output_population.append(kromosom)

    def calculate_error(self):
        self.error = []
        for i in range(len(self.hidden_population)):
            match = 0
            for j in range(len(dataset)):
                self.jst.set_weight(self.hidden_population[i], self.output_population[i])

                input_node = []
                for k in range(len(dataset[j])-1):
                    input_node.append(dataset[j][k])

                predicted_label = self.jst.calculate_output(input_node)
                label = dataset[j][len(dataset[j])-1]

                if predicted_label == label:
                    match = match + 1

            error = len(self.dataset)
            error = float((error - match))/len(self.dataset) * 100

            self.error.append(error)
        for i in range(len(self.error)):
            print i, " ", self.error[i]
        return 1

    def selection(self, type):

        if type == 1:
            # rank selection
            min_indexes = []
            min_values = nsmallest(10, self.error)
            print min_values
            for i in range(10):
                min_indexes.append(self.error.index(min_values[i]))
            return min_indexes
        elif type == 2:
            #roullete selection
            selected_parents = []
            #create finess value based on error
            fitness_value = []
            for i in range(len(self.error)):
                fitness_value.append(100-self.error[i])

            #check fitness value
            print "fitness_value :"
            for i in range(len(fitness_value)):
                print i, " ", fitness_value[i]


            #sum of fitnesses
            sum_fitnesses = 0
            for i in range(len(fitness_value)):
                sum_fitnesses = sum_fitnesses + fitness_value[i]

            #search for fixed point
            for i in range(10):
                random_number = random.random()*sum_fitnesses
                temp_sum = 0
                index_selected = -1
                for j in range(len(fitness_value)):
                    temp_sum = temp_sum + fitness_value[j]
                    if temp_sum > random_number:
                        index_selected = j
                        break
                print "i ",i
                selected_parents.append(index_selected)
            print "selection selected_parents ",selected_parents
            return selected_parents

        elif type == 3:
            #SUS selection
            selected_parents = []
            # create finess value based on error
            fitness_value = []
            for i in range(len(self.error)):
                fitness_value.append(100 - self.error[i])

            # check fitness value
            print "fitness_value :"
            for i in range(len(fitness_value)):
                print i, " ", fitness_value[i]

            # sum of fitnesses
            sum_fitnesses = 0
            for i in range(len(fitness_value)):
                sum_fitnesses = sum_fitnesses + fitness_value[i]

            #create 10 random number first
            random_numbers = []
            for i in range(10):
                random_numbers.append(random.random()*sum_fitnesses)

            for i in range(10):
                random_number = random_numbers[i]
                temp_sum = 0
                index_selected = -1
                for j in range(len(fitness_value)):
                    temp_sum = temp_sum + fitness_value[j]
                    if temp_sum > random_number:
                        index_selected = j
                        break
                print "i ",i
                selected_parents.append(index_selected)
            print "selection selected_parents ",selected_parents
            return selected_parents



    def crossover(self, type, parent_indexes):
        #one point crossover
        print parent_indexes
        if type == 1:
            new_hidden_population = []
            new_output_population = []

            for i in range(len(parent_indexes)):
                new_hidden_population.append(self.hidden_population[parent_indexes[i]])
                new_output_population.append(self.output_population[parent_indexes[i]])

            for i in range(len(parent_indexes)):
                for l in range(i+1, (len(parent_indexes))):
                    parent_1 = parent_indexes[i]
                    parent_2 = parent_indexes[l]

                    cross_point = random.randint(0, self.jst.num_hidden_node*self.jst.num_input_node-1)

                    kromosom_1 = []
                    kromosom_2 = []
                    for j in range(self.jst.num_hidden_node):
                        for k in range(self.jst.num_input_node):
                            value = self.hidden_population[parent_1][j][k]
                            kromosom_1.append(value)
                            value = self.hidden_population[parent_2][j][k]
                            kromosom_2.append(value)

                    for j in range(self.jst.num_hidden_node):
                        kromosom_1.append(self.output_population[parent_1][j])
                        kromosom_2.append(self.output_population[parent_2][j])

                    #print "parent index 1 ",parent_1
                    #print "parent index 2",parent_2
                    #print "kromosom 1 "
                    #print "\t".join(map(str, kromosom_1))
                    #print "kromosom 2 "
                    #print "\t".join(map(str, kromosom_2))
                    #print "cross point ",cross_point

                    new_kromosom_1 = []
                    new_kromosom_2 = []
                    for j in range(len(kromosom_1)):
                        if j<cross_point:
                            new_kromosom_1.append(kromosom_1[j])
                            new_kromosom_2.append(kromosom_2[j])
                        else:
                            new_kromosom_1.append(kromosom_2[j])
                            new_kromosom_2.append(kromosom_1[j])

                    #print "new k1 "
                    #print "\t".join(map(str,new_kromosom_1))
                    #print "new k2 "
                    #print "\t".join(map(str,new_kromosom_2))

                    child_1 = []
                    child_2 = []
                    for j in range(self.jst.num_hidden_node):
                        temp_1 = []
                        temp_2 = []

                        for k in range(self.jst.num_input_node):
                            temp_1.append(new_kromosom_1[j*self.jst.num_input_node+k])
                            temp_2.append(new_kromosom_2[j*self.jst.num_input_node+k])
                        child_1.append(temp_1)
                        child_2.append(temp_2)

                    output_child_1 = []
                    output_child_2 = []
                    for j in range(self.jst.num_hidden_node):
                        output_child_1.append(new_kromosom_1[self.jst.num_hidden_node*self.jst.num_input_node+j])
                        output_child_2.append(new_kromosom_2[self.jst.num_hidden_node * self.jst.num_input_node + j])

                    new_hidden_population.append(child_1)
                    new_output_population.append(output_child_1)
                    new_hidden_population.append(child_2)
                    new_output_population.append(output_child_2)

            self.hidden_population = new_hidden_population
            self.output_population = new_output_population
            return 1

        elif type == 2:
            new_hidden_population = []
            new_output_population = []

            for i in range(len(parent_indexes)):
                new_hidden_population.append(self.hidden_population[parent_indexes[i]])
                new_output_population.append(self.output_population[parent_indexes[i]])

            for i in range(len(parent_indexes)):
                for l in range(i+1, len(parent_indexes)):

                    #merandom parent yang digunakan
                    parent_1 = parent_indexes[i]
                    parent_2 = parent_indexes[l]

                    #merandom multiple cross point
                    cross_points = []
                    for j in range(10):
                        temp_point = random.randint(0, self.jst.num_hidden_node * self.jst.num_input_node - 1)
                        while temp_point in cross_points:
                            temp_point = random.randint(0, self.jst.num_hidden_node * self.jst.num_input_node - 1)
                        cross_points.append(temp_point)
                    cross_points.sort()
                    #print "cross points ",cross_points

                    #membangun kromosom induk
                    kromosom_1 = []
                    kromosom_2 = []
                    for j in range(self.jst.num_hidden_node):
                        for k in range(self.jst.num_input_node):
                            value = self.hidden_population[parent_1][j][k]
                            kromosom_1.append(value)
                            value = self.hidden_population[parent_2][j][k]
                            kromosom_2.append(value)

                    for j in range(self.jst.num_hidden_node):
                        kromosom_1.append(self.output_population[parent_1][j])
                        kromosom_2.append(self.output_population[parent_2][j])

                    #membangun kromosom anak dengan multiple crosspoint
                    new_kromosom_1 = []
                    new_kromosom_2 = []
                    flag = 0
                    for j in range(len(kromosom_1)):
                        if flag%2 == 0:
                            new_kromosom_1.append(kromosom_1[j])
                            new_kromosom_2.append(kromosom_2[j])
                        else:
                            new_kromosom_1.append(kromosom_2[j])
                            new_kromosom_2.append(kromosom_1[j])

                        if flag < len(cross_points) and j == cross_points[flag]:
                            flag = flag +1

                    child_1 = []
                    child_2 = []
                    for j in range(self.jst.num_hidden_node):
                        temp_1 = []
                        temp_2 = []

                        for k in range(self.jst.num_input_node):
                            temp_1.append(new_kromosom_1[j * self.jst.num_input_node + k])
                            temp_2.append(new_kromosom_2[j * self.jst.num_input_node + k])
                        child_1.append(temp_1)
                        child_2.append(temp_2)

                    output_child_1 = []
                    output_child_2 = []
                    for j in range(self.jst.num_hidden_node):
                        output_child_1.append(new_kromosom_1[self.jst.num_hidden_node * self.jst.num_input_node + j])
                        output_child_2.append(new_kromosom_2[self.jst.num_hidden_node * self.jst.num_input_node + j])

                    new_hidden_population.append(child_1)
                    new_output_population.append(output_child_1)
                    new_hidden_population.append(child_2)
                    new_output_population.append(output_child_2)

            self.hidden_population = new_hidden_population
            self.output_population = new_output_population
            return 1

    def write_to_file(self, generation):
        with open("output-data.csv", "a") as mycsvfile:
            thedatawriter = csv.writer(mycsvfile, dialect="mydialect")
            generation_string = "GENERATION "+str(generation)
            thedatawriter.writerow(generation_string)

            kromosom_population = []
            for i in range(len(self.hidden_population)):
                temp_kromosom = []
                temp_kromosom.append(i)
                for j in range(self.jst.num_hidden_node):
                    for k in range(self.jst.num_input_node):
                        temp_kromosom.append(self.hidden_population[i][j][k])
                for j in range(self.jst.num_hidden_node):
                    temp_kromosom.append(self.output_population[i][j])
                temp_kromosom.append(self.error[i])
                kromosom_population.append(temp_kromosom)

            for row in kromosom_population:
                thedatawriter.writerow(row)
            min_param = []
            min_value = nsmallest(1, self.error)
            min_index = self.error.index(min_value[0])
            min_param.append(min_index)
            min_param.append(min_value[0])
            thedatawriter.writerow(min_param)
            thedatawriter.writerow("\n")

    def evolve(self, num_iteration):
        file = open("output-data.csv", "w")
        file.close()
        for i in range(num_iteration):
            self.calculate_error()
            self.write_to_file(i)
            print "error ", min(self.error)

            #pilih selection dan crossover
            #selection 1: rank, 2:roullete, 3: SUS
            #crossover 1: one, 2: multipoint
            self.crossover(2, self.selection(2))

        print "finish"
        return 1


def loadDataset(filename, dataset):
    num_data = 0
    num_attribute = 0
    with open(filename) as file_stream:
        num_data = 0
        for line in file_stream:
            line = line.strip().split(",")
            data = []
            num_attribute = 0
            for i in range(len(line)):
                data.append(float(line[i]))
                num_attribute = num_attribute + 1
            num_data = num_data + 1
            dataset.append(data)

    result = (num_attribute-1, num_data)
    return result

def normalize(dataset, num_attribute):
    num_data = len(dataset)
    max_value_list = []

    for i in range(num_attribute):
        max_value = 0
        for j in range(num_data):
            if max_value < dataset[j][i]:
                max_value = dataset[j][i]
        max_value_list.append(max_value)

    for i in range(num_attribute):
        for j in range(num_data):
            dataset[j][i] = dataset[j][i]/max_value_list[i]

    return 1

if __name__ == '__main__':
    start_time = time.time()

    #loading dataset
    dataset = []
    result = loadDataset("mesothelimia-dataset.csv", dataset)
    print "fitur dan data ",result

    #normalisasi dataset
    normResult = normalize(dataset, result[0])

    #inisialisasi jst dengan 34 input node dan 5 hidden node
    myJst = Jst(result[0], 5)

    #testing perhitungan output JST
    input_node = []
    for i in range(result[0]):
        input_node.append(1)
    print "output : ", myJst.calculate_output(input_node)

    #testing GA
    myGa = Ga(myJst, dataset)
    myGa.evolve(10)

    print "execution time : ", time.time()-start_time