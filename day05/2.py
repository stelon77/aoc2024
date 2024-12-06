def rearrange(line, table):
    d = line.split(",")
    print(d)
    for i in range(len(d) - 1):
        j = i + 1
        while j < len(d):
        # for j in range(i, len(d)):
            if d[j] in table.keys():
                if d[i] in table[d[j]]:
                    a = d[j]
                    d[j] = d[i]
                    d[i] = a
                else:
                    j += 1
            else:
                j += 1
    # print(d)
    return int(d[len(d) // 2])



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
        error = 0
        while b and not error:
            c = b.pop()
            if b and (c in table.keys()):
                for val in table[c]:
                    if val in b:
                        error = 1
                        break
        if error:
            # print(rearrange(line, table))
            total += rearrange(line, table)


print(total)



