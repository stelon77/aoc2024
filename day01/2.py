from collections import Counter

total = 0
with open("input.txt") as fillin:
    lignes = fillin.readlines()
liste1 = []
liste2 = []
for ligne in lignes:
    data = ligne.split()
    liste1.append(int(data[0]))
    liste2.append(int(data[1]))
count2 = Counter(liste2)
count1 = Counter(liste1)
for key in count1.keys():
    total += key * count1[key] * count2[key]
print(total)
