import os
import re

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

stars = []

with open("input") as f:
    for line in f.readlines():
        match = re.search('position=<(?P<x>.*),(?P<y>.*)> velocity=<(?P<vx>.*),(?P<vy>.*)>', line)
        stars.append({key: int(match.group(key).strip()) for key in ["x", "y", "vx", "vy"]})
    f.close()

second = 9990

while True:
    min_x = 1000000
    min_y = 1000000
    max_x = 0
    max_y = 0
    for star in stars:
        star.update({"cx": star["x"] + (second * star["vx"])})
        star.update({"cy": star["y"] + (second * star["vy"])})

        if star["cx"] < min_x: min_x = star["cx"]
        if star["cy"] < min_y: min_y = star["cy"]

        if star["cx"] > max_x: max_x = star["cx"]
        if star["cy"] > max_y: max_y = star["cy"]


    if max_x <= 300:
        clear()

        for y in range(min_y, max_y + 1):
            line = ""
            for x in range(min_x, max_x + 1):
                pos_has_star = False
                for star in stars:
                    if star["cx"] == x and star["cy"] == y:
                        pos_has_star = True
                        break
                line += "#" if pos_has_star else "."
            print(line)
        print(min_x, min_y, max_x, max_y, second)

        input()

    print("Round %s finished. Dimensions: %sx%s" % (second, max_x, max_y))
    second += 1