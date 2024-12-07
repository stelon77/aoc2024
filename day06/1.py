def find_initial(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == "^":
                return(i, j, 0)
            if table[i][j] == ">":
                return(i, j, 1)
            if table[i][j] == "V":
                return(i, j, 2)
            if table[i][j] == "<":
                return(i, j, 3)
    return None

total = []

with open("input.txt") as fillin:
    lignes = fillin.readlines()
table = []
for line in lignes:
    table.append(line[:len(line) - 1])
(x, y, d) = find_initial(table)
# total.append((x, y))
# print(x, y, dir)
# while x >= 0 and x < len(table) and y >=0 and y < len(table[0]): #sinon sortie
while 1:
    if d == 0:
        if x == 0:
            total.append((x, y))
            print(len(set(total)))
            exit(0)
        elif table[x-1][y] == '#':
            d = 1
        else:
            total.append((x, y))
            x -= 1
    elif d == 1:
        if y == len(table[0]) -1:
            total.append((x, y))
            print(len(set(total)))
            exit(0)
        elif table[x][y + 1] == '#':
            d = 2
        else:
            total.append((x, y))
            y += 1
    elif d == 2:
        if x == len(table) - 1:
            total.append((x, y))
            print(len(set(total)))
            exit(0)
        elif table[x+1][y] == '#':
            d = 3
        else:
            total.append((x, y))
            x += 1
    elif d == 3:
        if y == 0:
            total.append((x, y))
            print(len(set(total)))
            exit(0)
        elif table[x][y - 1] == '#':
            d = 0
        else:
            total.append((x, y))
            y -= 1







