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

        points.append({"x": x, "y": y, "area": 0, "inf": False})
    f.close()

for x in range(max_x + 1):
    for y in range(max_y + 1):
        print("%s,%s" % (x, y))
        distances = []
        for p in points:
            d = abs(x - p["x"]) + abs(y - p["y"])
            distances.append({"d": d, "p": p})
        min_distance = min(distances, key=lambda x: x["d"])
        num_min_distance = len([x for x in distances if x["d"] == min_distance["d"]])
        if not (x > 0 and x < max_x and y > 0 and y < max_y):
            min_distance["p"]["inf"] = True
        if num_min_distance == 1:
            min_distance["p"]["area"] += 1

max_area = 0
for p in points:
    if not p["inf"]:
        if p["area"] > max_area: max_area = p["area"]
print()
print(max_area)