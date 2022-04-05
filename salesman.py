from xmlrpc.client import MultiCallIterator
import numpy as np
import pygad
import pandas as pd 

def convert_array_to_list(array):

    array_list = []
    for l in array:
        array_list.extend(l)

    return array_list

def find_smallest_distance(array):

    array_list = convert_array_to_list(array)    
    array_list.sort()
    mylist = list(dict.fromkeys(array_list))
    
    min_distance = 0
    max_distance = 0

    for i in mylist[0:8]:
        min_distance += i

    for j in mylist[-7:]:
        max_distance += j

    return min_distance, max_distance

def calc_distance(route):
    
    distance = 0.0
    cities_visited = [0]    # adiciona primeira cidade com 0

    # print (route)

    for n in route:    
        if n in cities_visited:
            distance += 10000   

        # print ('___________-')
        # print (cities_visited)
        # print ('last', cities_visited[len(cities_visited)-1])
        # print ('n', n)
        # print (cities[cities_visited[len(cities_visited)-1]][n])

        distance += cities[cities_visited[len(cities_visited)-1]][n]
                
        cities_visited.append(n)
        # print (cities_visited)

    distance += cities[cities_visited[len(cities_visited)-1]][0]

    # print (distance)

    return distance

def fitness(route, index):

    min_distance, max_distance = find_smallest_distance (cities)    
    return 1/((calc_distance(route)-min_distance)/(max_distance-min_distance)) # normalization

# Load data
cities = pd.read_csv('matrix_distances.csv', header=None).values.tolist()

# Estrutura da solucao
gene_space              = [1,2,3,4,5,6,7]
gene_type               = int
num_genes               = 7
num_generations         = 100

# Parametros de populacao
sol_per_pop             = 100               # numero de interaçoes
parent_selection_type   = 'rws'              
crossover_type          = 'single_point'
mutation_type           = 'scramble'
mutation_probability    = 0.1             # percentagem
num_parents_mating      = 50              # selecao de pais por interacao
keep_parents            = 1               # elitismo - bom para quando nao converge rapidamente. 

# atributos de configuracao do algoritmo
save_best_solutions     = True
save_solutions          = True
fitness_func            = fitness


ga_instance = pygad.GA(
    num_generations=num_generations,
    gene_space=gene_space,
    gene_type=gene_type,
    num_genes=num_genes,
    sol_per_pop=sol_per_pop,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_probability=mutation_probability,
    num_parents_mating=num_parents_mating,
    save_best_solutions=save_best_solutions,
    save_solutions=save_solutions,
    fitness_func=fitness_func,
)

ga_instance.run()
ga_instance.plot_fitness()
# ga_instance.plot_genes()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Best distance = {distance}".format(distance=calc_distance(solution)))

# route_test = [1,3,2,5,7,4,6] # nao incluir 0
# fitness(route_test, 1)

# resultado dominante e muito rapido - necessario alterar os parametros do algoritmo
# proxima aula:
# aumentar variabilidade dos genes 
# modificar a taxa de mutacao 

# resultado otimizado utilizando mutation_type = 'scramble'. Os outros types nao chegaram a produzir um resultado otimizado






