BLINKS = 5

def blinking25(list0):
    for blink in range(BLINKS):
        # print(blink)
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
    return(list0)

total = 0
table = []
with open("i.txt") as fillin:
    lignes = fillin.readlines()
list0 = lignes[0][:-1].split()
list25 = blinking25(list0)

# print()
dict25 = {}
for n in list25:
    if n in dict25.keys():
        dict25[n] += 1
    else:
        dict25[n] = 1
# print(dict25)
# print(len(dict25))
for item in list0:
    if item in dict25.keys():
        print("True")
    else:
        print("False")