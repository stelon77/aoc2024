wide = 101
tall = 103
seconds = 100
E = wide // 2
N = tall // 2


# total = 1
# quadrants = {
#     'SO': 0, 'SE': 0, 'NO': 0, 'NE':0
# }
with open("i.txt") as fillin:
    lignes = fillin.readlines()

for i in range(100000):
    total = 1
    quadrants = {
    'SO': 0, 'SE': 0, 'NO': 0, 'NE':0
}
    for line in lignes:
        rob = line[:-1].split()
        init = rob[0][2:].split(",")
        x0 = int(init[0])
        y0 = int(init[1])
        move = rob[1][2:].split(",")
        vx = int(move[0])
        vy = int(move[1])
        xend = (x0 + vx * seconds) % wide
        yend = (y0 + vy * seconds) % tall
        # print(xend, yend)
        # print(wide // 2)
        if xend < E and yend < N:
            quadrants["NO"] += 1
            # print("yo")
        elif xend < E and yend > N:
            quadrants["SO"] += 1
            # print("ya")
        elif xend > E and yend < N:
            quadrants["NE"] += 1
        #     print("yu")
        elif xend > E and yend > N:
            quadrants["SE"] += 1
            # print("yi")
    # print(quadrants)
    print(i)
    if quadrants["NE"] == quadrants["NO"] and quadrants["SE"] == quadrants["SO"]:
        print ("..........................")
        exit(0)