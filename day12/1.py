total = 0
table = []
with open("i.txt") as fillin:
    lignes = fillin.readlines()
for line in lignes:
    elts = []
    for elt in line[:-1]:
        elts.append(elt)
    table.append(elts)

xmax = len(table)
ymax = len(table[0])
# print(xmax, ymax)

dejaUtilise = []
for i in range(xmax):
    for j in range(ymax):
        aire = 0
        cloture = 0
        enCours = []
        memeElt = []
        # initialisation
        if (i, j) in dejaUtilise:
            continue
        elt = table[i][j]
        enCours.append((i, j))
        while enCours:
            aire += 1
            (x, y) = enCours.pop()
            memeElt.append((x, y))
            #nord
            if x - 1 == -1:
                # print("N")
                cloture += 1
            else:
                if (x - 1, y) in enCours or (x - 1, y) in memeElt or (x - 1, y) in dejaUtilise:
                    if (x - 1, y) in dejaUtilise:
                        cloture += 1
                else:
                    if table[x - 1][y] == elt:
                        enCours.append((x - 1, y))
                    else:
                        # print("N")
                        cloture += 1
            #sud
            if x + 1 == xmax:
                # print("S")
                cloture += 1
            else:
                if (x + 1, y) in enCours or (x + 1, y) in memeElt or (x + 1, y) in dejaUtilise:
                    if (x + 1, y) in dejaUtilise:
                        cloture += 1

                else:
                    if table[x + 1][y] == elt:
                        enCours.append((x + 1, y))
                    else:
                        # print("S")
                        cloture += 1
            #ouest
            if y - 1 == -1:
                cloture += 1
            else:
                if (x, y - 1) in enCours or (x, y - 1) in memeElt or (x, y - 1) in dejaUtilise:
                    if (x, y - 1) in dejaUtilise:
                        cloture += 1
                else:
                    if table[x][y - 1] == elt:
                        enCours.append((x, y - 1))
                    else:
                        cloture += 1
            #est
            if y + 1 == ymax:
                cloture += 1
            else:
                if (x, y + 1) in enCours or (x, y + 1) in memeElt or (x, y + 1) in dejaUtilise:
                    if (x, y + 1) in dejaUtilise:
                        cloture += 1
                else:
                    if table[x][y + 1] == elt:
                        enCours.append((x, y + 1))
                    else:
                        cloture += 1

        dejaUtilise = dejaUtilise + memeElt
        memeElt.clear()
        print(i, j)
        # print("clot =", cloture)
        # print("aire = ", aire)
        total += cloture * aire

print(total)




