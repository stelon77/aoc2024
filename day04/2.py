def checkXMAS(n, m, table):
    total = 0
    maxn = len(table) - 1
    maxm = len(table[0]) - 1
    # horizontal
    if table[n+1][m+1] == 'M' and table[n-1][m-1] == 'S' and table[n+1][m-1] == 'M' and table[n-1][m+1] == 'S':
        total += 1
    if table[n+1][m+1] == 'S' and table[n-1][m-1] == 'M' and table[n+1][m-1] == 'M' and table[n-1][m+1] == 'S':
        total += 1
    if table[n+1][m+1] == 'M' and table[n-1][m-1] == 'S' and table[n+1][m-1] == 'S' and table[n-1][m+1] == 'M':
        total += 1
    if table[n+1][m+1] == 'S' and table[n-1][m-1] == 'M' and table[n+1][m-1] == 'S' and table[n-1][m+1] == 'M':
        total += 1
    return total


total = 0
with open("input.txt") as fillin:
    lignes = fillin.readlines()
table = []
for line in lignes:
    table.append(line[:len(line) - 1])
# print(table)
length = len(table[0])

hight = len(table)
# print(hight)
for n in range(1, hight - 1):
    for m in range(1, length - 1):
        # print(n, m)
        if table[n][m] == 'A':
            total += checkXMAS(n, m, table)
print(total)





