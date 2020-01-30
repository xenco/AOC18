serial = 3628
gridsize = 300

cells = [[0 for x in range(gridsize)] for y in range(gridsize)]

for x in range(gridsize):
    for y in range(gridsize):
        cells[x][y] = ((((x + 1) + 10) * (y + 1) + serial) * ((x + 1) + 10) // 100) % 10 - 5

cell_powers = []
for y in range(gridsize - 2):
    for x in range(gridsize - 2):
        power = sum([
                cells[y][x], cells[y][x + 1], cells[y][x + 2],
                cells[y + 1][x], cells[y + 1][x + 1], cells[y + 1][x + 2],
                cells[y + 2][x], cells[y + 2][x + 1], cells[y + 2][x + 2]
            ])
        cell_powers.append({"top_left": str(y+1)+","+str(x+1), "power": power})

print(max(cell_powers, key=lambda x: x["power"]))