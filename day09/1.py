from itertools import *


total = []
table = {}
with open("e.txt") as fillin:
    lignes = fillin.readlines()
line = lignes[0]
maxId = len(line[::2]) - 1
maxIndex = -1
for c in line[::2]:
    maxIndex += int(c)
print(maxIndex)

line = list(line)
mult = []
for i in range(maxIndex):
    mult.append(i % maxId)
print(mult)





# print(line)
# print(maxId)
# print(len(line))
