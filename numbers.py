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

individual = []
minimal  = 1000000

n = int(input())

for i in input().split():
    #value = int(i)
    individual.append(int(i))


n = 0
while n < 100000:
    newValue = fitness(individual)
    aux = crossover(individual)[0] + crossover(individual)[1]
    mutation(aux)
    
    minimal    = min(minimal, newValue) 
    individual = aux

    n = n + 1

print(minimal)