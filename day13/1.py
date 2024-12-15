

total = 0
table = []
with open("i.txt") as fillin:
    lignes = fillin.readlines()
table = []
for i in range((len(lignes)+1) // 4):
    datas = []
    a = lignes[i * 4][:-1].split(":")
    data = a[1].split(",")
    A =(int(data[0][3:]), int(data[1][3:]))
    datas.append(A)
    b = lignes[i * 4 + 1][:-1].split(":")
    data = b[1].split(",")
    B =(int(data[0][3:]), int(data[1][3:]))
    datas.append(B)
    p = lignes[i * 4 + 2][:-1].split(":")
    data = p[1].split(",")
    P =(int(data[0][3:]), int(data[1][3:]))
    datas.append(P)
    table.append(datas)

for i, t in enumerate(table):
    print(i)
    solutions = []
    for a in range(101):
        for b in range(101):
            if (a * t[0][0] + b * t[1][0] == t[2][0]) and (a * t[0][1] + b * t[1][1] == t[2][1]):
                solutions.append(a * 3 + b)
    if solutions:
        print(solutions)
        total += max(solutions)
print(total)








