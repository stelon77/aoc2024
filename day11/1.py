BLINKS = 25

total = 0
table = []
with open("e.txt") as fillin:
    lignes = fillin.readlines()
list0 = lignes[0][:-1].split()
for blink in range(BLINKS):
    print(blink)
    listing = []
    for item in list0:
        if item == "0":
            listing.append("1")
        elif len(item) % 2 == 0:
            item1 = item[:len(item)// 2]
            item2 = item[len(item)// 2:]
            listing.append(str(int(item1)))
            listing.append(str(int(item2)))
        else:
            listing.append(str(int(item) * 2024))
    list0 = listing
print(list0)
print(len(list0))