import numpy as np
import pygad as ga
import pandas as pd 

cities = pd.read_csv('matrix_distances.csv', header=None).values.tolist()

print (cities)

def fitness(route):

    distance = 0.0
    cities_visited = [0]

    for n in route:
        
        distance += cities[len(cities_visited)-1][n]
        cities_visited.append(n)
        print (cities_visited)

    return 1/distance

route_test = [3,2,1,4,5,6,7,0]

print (fitness(route_test))