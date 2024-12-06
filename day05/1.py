

total = 0
table = {}
with open("input.txt") as fillin:
    lignes = fillin.readlines()
first = 0
for line in lignes:
    # print(len(line))
    line = line[:-1]
    if "|" in line:
        a = line.split("|")
        if a[0] in table.keys():
            table[a[0]].append(a[1])
        else:
            table[a[0]] = [a[1]]
    elif "," in line:
        b = line.split(",")
        nb = int(b[len(b)//2])
        error = 0
        while b and not error:
            c = b.pop()
            if b and (c in table.keys()):
                for val in table[c]:
                    if val in b:
                        error = 1
                        break
        if not error:
            total += nb
print(total)


