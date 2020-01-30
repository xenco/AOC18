max_x = 0
max_y = 0

points = []

with open("input") as f:
    for line in f.readlines():
        l = line.strip().split(", ")
        x = int(l[0])
        y = int(l[1])

        if x > max_x: max_x = x
        if y > max_y: max_y = y

        points.append({"x": x, "y": y})
    f.close()

area = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        print("%s,%s" % (x, y))
        distances = []
        for p in points:
            d = abs(x - p["x"]) + abs(y - p["y"])
            distances.append({"d": d, "p": p})
        sum_distance = 0
        for d in distances:
            sum_distance += d["d"]

        if(sum_distance < 10000):
            area += 1
print()
print(area)