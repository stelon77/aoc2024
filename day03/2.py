total = 0
with open("input.txt") as fillin:
    lignes = fillin.readlines()
mult = 1
for line in lignes:
    
    a = line.split("mul(")
    # print(a)
    for elt in a:
        b = elt.split(")")[0]
        if "," in  b:
            c = b.split(",", 1)
            if c[0].isnumeric() and c[1].isnumeric() and int(c[0]) < 1000 and int(c[1]) < 1000:
                total += int(c[0]) * int(c[1]) * mult
        # print(elt)

        if "don't()" in elt:
            mult = 0
        elif "do()" in elt:
            mult = 1
        else:
            pass
print(total)