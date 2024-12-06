def checkXMAS(n, m, table):
    total = 0
    maxn = len(table) - 1
    maxm = len(table[0]) - 1
    # horizontal
    if m <= maxm - 3 and table[n][m+1] == 'M' and table[n][m+2] == 'A' and table[n][m+3] == 'S':
        total += 1
    if m >=  3 and table[n][m-1] == 'M' and table[n][m-2] == 'A' and table[n][m-3] == 'S':
        total += 1
    # vertical
    if n <= maxn - 3 and table[n + 1][m] == 'M' and table[n +  2][m] == 'A' and table[n + 3][m] == 'S':
        total += 1
    if n >=  3 and table[n-1][m] == 'M' and table[n-2][m] == 'A' and table[n-3][m] == 'S':
        total += 1
    # diagonale se-no
    if m <= maxm - 3 and n <= maxn - 3 and table[n+1][m+1] == 'M' and table[n+2][m+2] == 'A' and table[n+3][m+3] == 'S':
        total += 1
    if m >=  3 and n >= 3 and table[n-1][m-1] == 'M' and table[n-2][m-2] == 'A' and table[n-3][m-3] == 'S':
        total += 1
    # diagonale ne-so
    if m <= maxm - 3 and n >= 3 and table[n-1][m+1] == 'M' and table[n-2][m+2] == 'A' and table[n-3][m+3] == 'S':
        total += 1
    if m >=  3 and n <= maxn - 3 and table[n+1][m-1] == 'M' and table[n+2][m-2] == 'A' and table[n+3][m-3] == 'S':
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
for n in range(hight):
    for m in range(length):
        # print(n, m)
        if table[n][m] == 'X':
            total += checkXMAS(n, m, table)
print(total)





