with open("input.txt") as fillin:
    lignes = fillin.readlines()
liste1 = []
liste2 = []
for ligne in lignes:
    data = ligne.split()
    liste1.append(int(data[0]))
    liste2.append(int(data[1]))
liste1.sort()
liste2.sort()
total = 0
for x, y in zip(liste1, liste2):
    total += abs(x-y)
print(total)