import copy

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

def returnlist(x, y, d, table):
    total = []
    while 1:
        if d == 0:
            if x == 0:
                total.append((x, y))
                return(list(set(total)))
            elif table[x-1][y] == '#':
                d = 1
            else:
                total.append((x, y))
                x -= 1
        elif d == 1:
            if y == len(table[0]) -1:
                total.append((x, y))
                return(list(set(total)))

            elif table[x][y + 1] == '#':
                d = 2
            else:
                total.append((x, y))
                y += 1
        elif d == 2:
            if x == len(table) - 1:
                total.append((x, y))
                return(list(set(total)))

            elif table[x+1][y] == '#':
                d = 3
            else:
                total.append((x, y))
                x += 1
        elif d == 3:
            if y == 0:
                total.append((x, y))
                return(list(set(total)))
            elif table[x][y - 1] == '#':
                d = 0
            else:
                total.append((x, y))
                y -= 1

def trial(tab, x, y , d):
    total = []
    # print("coucou")
    # print(tab)
    while 1:
        if d == 0:
            if x == 0:
                return(0)
            elif tab[x-1][y] == '#':
                d = 1
            else:
                if (x, y, d) in total:
                    return(1)
                total.append((x, y, d))
                x -= 1

        elif d == 1:
            if y == len(tab[0]) -1:
                return(0)
            elif tab[x][y + 1] == '#':
                d = 2
            else:
                if (x, y, d) in total:
                    return(1)
                total.append((x, y, d))
                y += 1

        elif d == 2:
            if x == len(tab) - 1:
                return(0)
            elif tab[x+1][y] == '#':
                d = 3
            else:
                if (x, y, d) in total:
                    return(1)
                total.append((x, y, d))
                x += 1

        elif d == 3:
            if y == 0:
                return(0)
            elif tab[x][y - 1] == '#':
                d = 0
            else:
                if (x, y, d) in total:
                    return(1)
                total.append((x, y, d))
                y -= 1


total = 0

with open("input.txt") as fillin:
    lignes = fillin.readlines()
table = []
for line in lignes:
    ligne = []
    for char in line:
        ligne.append(char)
    table.append(ligne)
    # table.append(line[:len(line) - 1])
(x, y, d) = find_initial(table)
plots = returnlist(x, y, d, table)
pos0 = (x, y, d)
# print(plots)
plots.remove((pos0[0], pos0[1]))
# print(plots)


# print(x, y, dir)
# while x >= 0 and x < len(table) and y >=0 and y < len(table[0]): #sinon sortie
# for i in range(len(table[0])):
# # for i in range(2):
#     for j in range(len(table)):
#         print(i, j)
for i, plot in enumerate(plots):
    print(i)

    # for j in range(2):
        # print("table")
        # print(table)
    tab = copy.deepcopy(table)
        # for item in table:
        #     tab.append(item)

    if tab[plot[0]][plot[1]] == ".":
        tab[plot[0]][plot[1]] = "#"
        # print("coucou")
        # print(tab)
    total += trial(tab, pos0[0], pos0[1], pos0[2])
print(total)








