import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fitness(aList):
    k = len(aList) // 2

    father = aList[:k]
    mother = aList[k:]
    
    result = 1
    for a in mother:
        result = result*a

    return abs(sum(father)**2 - result)


def mutation(aList):
    pos1 = random.randint(0, len(aList) - 1)
    pos2 = random.randint(0, len(aList) - 1)

    aList[pos1], aList[pos2] = aList[pos2], aList[pos1]

def crossover(aList):
    k = len(aList) // 2

    father = aList[:k]
    mother = aList[k:]
    
    m = len(father) // 2

    return (father[:m] + mother[m:], mother[:m] + father[m:])

numbers    = []
population = []

minimo = 1000000

n = int(input())

for i in input().split():
    #value = int(i)
    numbers.append(int(i))


population.append(numbers)

n = 0
while n < 100000:
    aux = []

    for individual in population:
        newValue = fitness(individual)

        if newValue < minimo:
            minimo = newValue
        
        aux = crossover(individual)[0] + crossover(individual)[1]
        mutation(aux)

    population = []
    if len(aux) != 0:
        population.append(aux)
    
    #print(f"{population}", file=sys.stderr)
    n = n + 1


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(minimo)
