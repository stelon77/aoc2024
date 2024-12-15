total = 0
table = {}
with open("i.txt") as fillin:
    lignes = fillin.readlines()
line = lignes[0]
extension = []
compacted = []
maxindex = 0
for i, c in enumerate(line):
    # print(i)
    if i % 2:
        for k in range(int(c)):
            extension.append(".")
    else:
        maxindex += int(c)
        nb = str(i // 2)

        for k in range(int(c)):
            # print(str(i // 2))
            extension.append(nb)
            compacted.append(nb)
print("etape 1 terminee")
# print(compacted)

final = []
for j in range(maxindex):
    if extension[j] != ".":
        final.append(extension[j])
    else:
        final.append(compacted.pop())
print(final)
print("etape 2 terminee")

for n, val in enumerate(final):
    total += n * int(val)
print(total)









# print(line)
# print(maxId)
# print(len(line))
