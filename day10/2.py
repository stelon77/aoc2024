def check(table, i, j, xmax, ymax):
    n = 0
    arrivees = []
    cases = [(i, j, n)]
    utilisees = []
    while len(cases) != 0:
        #on tourne autour
        X = cases[0][0]
        Y = cases[0][1]
        C = cases[0][2]
        if X > 0 and int(table[X - 1][Y]) == C + 1:
            if C + 1 == 9:
                arrivees.append((X - 1, Y))
            else:
                cases.append((X - 1, Y, C + 1))

        if Y > 0 and int(table[X][Y - 1]) == C + 1:
            if C + 1 == 9:
                arrivees.append((X, Y - 1))
            else:
                cases.append((X, Y - 1, C + 1))

        if X < xmax - 1 and int(table[X + 1][Y]) == C + 1:
            if C + 1 == 9:
                arrivees.append((X + 1, Y))
            else:
                cases.append((X + 1, Y, C + 1))

        if Y < ymax -1 and int(table[X][Y + 1]) == C + 1:
            if C + 1 == 9:
                arrivees.append((X, Y + 1))
            else:
                cases.append((X, Y + 1, C + 1))

        cases.pop(0)

    return(len((arrivees)))


total = 0
table = []
with open("i.txt") as fillin:
    lignes = fillin.readlines()
for line in lignes:
    table.append(line[:-1])
    # print(table)
xmax = len(table)
ymax = len(table[0])
for i in range(xmax):
    for j in range(ymax):
        if table[i][j] == "0":
            total += check(table, i, j, xmax, ymax)
print(total)

