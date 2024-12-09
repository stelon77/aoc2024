from itertools import *

def check(numbers, n, goal):
    table = list(product("ABC", repeat= n))
    # print(table)
    for tab in table:
        tot = int(numbers[0])
        for i in range(n):
            if tab[i] == "A":
                tot += int(numbers[i + 1])
            elif tab[i] == "B":
                tot *= int(numbers[i + 1])
            elif tab[i] == "C":
                tot = int(str(tot) + numbers[i + 1])
        if tot == goal:
            return(goal)
    return(0)

total = 0
table = {}
with open("i.txt") as fillin:
    lignes = fillin.readlines()
for z, line in enumerate(lignes):
    print(z)
    nbs = line.split(":")
    goal = int(nbs[0])
    numbers = nbs[1][1:-1].split()
    # print(numbers)
    n = len(numbers) - 1
    total += check(numbers, n, goal)
print(total)
