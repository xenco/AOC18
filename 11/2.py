from blist import blist

cells = [[((((x + 1) + 10) * (y + 1) + 3628) * ((x + 1) + 10) // 100) % 10 - 5 for x in range(300)] for y in range(300)]
cell_powers = blist([])

for size in range(1, 301):
    for size in range(1, 301):
        for y in range(300 - (size - 1)):
            for x in range(300 - (size - 1)):
                cell_powers.append({ "top_left": str(y + 1) + "," + str(x + 1), "power": sum(blist([cells[y + sy][x + sx] for sx in range(size) for sy in range(size)])), "size": size })
        print(size, max(cell_powers, key=lambda x: x["power"]))
max_power = max(cell_powers, key=lambda x: x["power"])
print(max_power["top_left"] + "," + str(max_power["size"]))
