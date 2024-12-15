def findCloture(memeElt,xmax, ymax):
    clot = 0
    for point in memeElt:
        x = point[0]
        y = point[1]

        #nord
        if (x-1, y) not in memeElt:
            if (x, y-1) in memeElt and (x - 1, y - 1) in memeElt:
                clot += 1
            elif (x, y - 1) not in memeElt:
                clot += 1
        # sud
        if (x+1, y) not in memeElt:
            if (x, y + 1) in memeElt and (x + 1, y + 1) in memeElt:
                clot += 1
            elif (x, y + 1) not in memeElt:
                clot += 1
        # est
        if (x, y + 1) not in memeElt:
            if (x - 1, y) in memeElt and (x - 1, y + 1) in memeElt:
                clot += 1
            elif (x - 1, y) not in memeElt:
                clot += 1
        # ouest
        if (x, y - 1) not in memeElt:
            if (x + 1, y) in memeElt and (x + 1, y - 1) in memeElt:
                clot += 1
            elif (x + 1, y) not in memeElt:
                clot += 1
    # print("clot =", clot)
    return(clot)


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
        print(i)
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
                # cloture += 1
                pass
            else:
                if (x - 1, y) in enCours or (x - 1, y) in memeElt or (x - 1, y) in dejaUtilise:
                    pass
                    # if (x - 1, y) in dejaUtilise:
                    #     cloture += 1
                else:
                    if table[x - 1][y] == elt:
                        enCours.append((x - 1, y))
                    else:
                        pass
                        # print("N")
                        # cloture += 1
            #sud
            if x + 1 == xmax:
                # print("S")
                # cloture += 1
                pass
            else:
                if (x + 1, y) in enCours or (x + 1, y) in memeElt or (x + 1, y) in dejaUtilise:
                    pass
                    # if (x + 1, y) in dejaUtilise:
                    #     cloture += 1

                else:
                    if table[x + 1][y] == elt:
                        enCours.append((x + 1, y))
                    else:
                        # print("S")
                        # cloture += 1
                        pass
            #ouest
            if y - 1 == -1:
                # cloture += 1
                pass
            else:
                if (x, y - 1) in enCours or (x, y - 1) in memeElt or (x, y - 1) in dejaUtilise:
                    # if (x, y - 1) in dejaUtilise:
                    #     cloture += 1
                    pass
                else:
                    if table[x][y - 1] == elt:
                        enCours.append((x, y - 1))
                    else:
                        # cloture += 1
                        pass
            #est
            if y + 1 == ymax:
                # cloture += 1
                pass
            else:
                if (x, y + 1) in enCours or (x, y + 1) in memeElt or (x, y + 1) in dejaUtilise:
                    pass
                    # if (x, y + 1) in dejaUtilise:
                    #     cloture += 1
                else:
                    if table[x][y + 1] == elt:
                        enCours.append((x, y + 1))
                    else:
                        # cloture += 1
                        pass
        #il faut trouver la cloture avec memeElt
        cloture = findCloture(memeElt, xmax, ymax)
        dejaUtilise = dejaUtilise + memeElt
        memeElt.clear()
        # print(i, j)
        # print("clot =", cloture)
        # print("aire = ", aire)
        total += cloture * aire

print(total)