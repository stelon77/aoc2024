from itertools import *


total = []
table = {}
with open("i.txt") as fillin:
    lignes = fillin.readlines()
for i, line in enumerate(lignes):
    for j, char in enumerate(line[:-1]):
        if char != ".":
            if char in table.keys():
                table[char].append((i, j))
            else:
                table[char] = [(i, j)]
# print(table)
xmax = len(lignes)
# print("xmax =", xmax)
ymax = len(lignes[0]) - 1
# print("ymax =", ymax)

for value in table.values():
    if len(value) == 1:
        break
    total += value
    couples = list(combinations(value, 2))
    for couple in couples:
        x = couple[0][0] - couple[1][0]
        y = couple[0][1] - couple[1][1]

        x1 = couple[0][0] + x
        y1 = couple[0][1] + y
        while x1 >= 0 and x1 < xmax and y1 >= 0 and y1 < ymax:
            # print("x1",couple, x1, y1)
            total.append((x1, y1))
            x1 = x1 + x
            y1 = y1 + y

        x2 = couple[1][0] - x
        y2 = couple[1][1] - y
        while x2 >= 0 and x2 < xmax and y2 >= 0 and y2 < ymax:
            # print("x2",couple, x2, y2, x1, y1)
            total.append((x2, y2))
            x2 = x2 - x
            y2 = y2 - y

# print((set(total)))
print(len(set((total))))




