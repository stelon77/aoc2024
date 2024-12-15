

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
    P =(int(data[0][3:]) + 10000000000000, int(data[1][3:]) + 10000000000000)
    datas.append(P)
    table.append(datas)

for i, t in enumerate(table):
    print(i)
    B = (t[2][0] * t[0][1] - t[2][1] * t[0][0]) // ((t[1][0] * t[0][1]) - (t[0][0] * t[1][1]))
    A = (t[2][0] - (B * t[1][0])) // t[0][0]

    if A >= 0 and B >= 0 and t[0][0] * A + t[1][0] * B == t[2][0] and t[0][1] * A + B * t[1][1] == t[2][1]:
        total += A * 3 + B
        print("ok")
    
print(total)








