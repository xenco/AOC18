# 71,123
class Cart():
    def __init__(self, x, y, direction):
        self.x, self.y, self.direction = x, y, direction  # 0=up, 1=down, 2=left, 3=right
        self.c_turn = 1
        self.crashed = False

    def move(self):
        new_y = self.y - 1 if self.direction == 0 else (self.y + 1 if self.direction == 1 else self.y)
        new_x = self.x - 1 if self.direction == 2 else (self.x + 1 if self.direction == 3 else self.x)

        self.x, self.y = new_x, new_y

        if field[new_y][new_x] == "\\":
            self.direction = (self.direction + 2) % 4
        elif field[new_y][new_x] == "/":
            self.direction = 3 - self.direction
        elif field[new_y][new_x] == "+":
            turn_delta = [[2, 3], [3, 2], [1, 0], [0, 1]]
            self.direction = turn_delta[self.direction][0] if self.c_turn == 1 else (turn_delta[self.direction][1] if self.c_turn == 3 else self.direction)
            self.c_turn = self.c_turn + 1 if self.c_turn < 3 else 1

current_tick = 0
field = [[c if c != '_' else ' ' for c in line.strip("\n")] for line in open("input_real").readlines()]

carts = []
for y in range(150):
    for x in range(150):
        try:
            cart = Cart(x, y, ["^", "v", "<", ">"].index(field[y][x]))
            carts.append(cart)
            field[y][x] = "|" if cart.direction <= 1 else "-"  # fix map positions where carts are
        except ValueError:  # current char is not a cart
            pass

while True:
    current_tick += 1

    carts.sort(key=lambda c: c.x)
    carts.sort(key=lambda c: c.y)

    for cart1 in carts:
        if not cart1.crashed:
            cart1.move()
            for cart2 in carts:
                if not cart2.crashed:
                    if not (cart1 is cart2) and (cart1.x == cart2.x and cart1.y == cart2.y):
                        cart1.crashed = True
                        cart2.crashed = True

    available_carts = [c for c in carts if not c.crashed]
    if len(available_carts) == 1:
        print("Only one cart left at %s,%s" % (available_carts[0].x, available_carts[0].y))
        raise SystemExit

    print("\rTick: %s, Carts: %s" % (current_tick, len([c for c in carts if not c.crashed])))
