from colorama import init

init()

import os
import time
import copy

clear = lambda: os.system('cls')

cart_symbols = ["^", "v", "<", ">"]

class Field():
    def __init__(self, input):
        self.current_tick = 0
        self.data = [[c if c != '_' else ' ' for c in line.strip("\n")] for line in open(input).readlines()]
        self.max_x, self.max_y = max([len(x) for x in self.data]), len(self.data)

        self.carts = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                try:
                    cart = Cart(x, y, cart_symbols.index(self.data[y][x]))
                    self.carts.append(cart)
                    self.data[y][x] = "|" if cart.direction <= 1 else "-"  # fix map positions where carts are
                except ValueError:  # current char is not a cart
                    pass

    def __str__(self):
        return ("Tick: %s\n" % self.current_tick + '\n'.join([''.join([self.data[y][x] for x in range(self.max_x)]) for y in range(self.max_y)]))

    def tick(self):
        for cart in self.carts:
            cart.move()
            collision = self.collision()
            if collision:
                print("Collision occured at %s,%s" % (collision[0], collision[1]))
                raise SystemExit
        self.current_tick += 1
        # self.print()
        return False

    def collision(self):
        collision = False
        for cart1 in self.carts:
            for cart2 in self.carts:
                if (not cart1 is cart2) and (cart1.x == cart2.x and cart1.y == cart2.y):
                    collision = (cart1.x, cart1.y)
        return collision

    def print(self):
        print_field = copy.deepcopy(self.data)
        for cart in self.carts:
            print_field[cart.y][cart.x] = '\033[31m' + cart_symbols[cart.direction] + '\033[0m'
        print("Tick: %s\n" % self.current_tick + '\n'.join([''.join([print_field[y][x] for x in range(self.max_x)]) for y in range(self.max_y)]))

    def __getitem__(self, pos):
        x, y = pos
        return self.data[y][x]

    def __setitem__(self, pos, value):
        x, y = pos
        self.data[y][x] = value

class Cart():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction  # 0=up, 1=down, 2=left, 3=right
        self.c_turn = 1
        self.id = 1

    def move(self):
        new_x = self.x
        new_y = self.y

        if self.direction == 0:
            new_y -= 1  # move up
        elif self.direction == 1:
            new_y += 1  # move down
        elif self.direction == 2:
            new_x -= 1  # move left
        elif self.direction == 3:
            new_x += 1  # move right

        # what is at new_x,new_y
        new_field = field[new_x, new_y]
        if new_field == "\\":  # turn
            self.direction = (self.direction + 2) % 4
        elif new_field == "/":  # turn
            self.direction = 3 - self.direction
        elif new_field == "+":  # intersection logic
            for i, d in enumerate([[2, 3], [3, 2], [1, 0], [0, 1]]):
                if self.direction == i:
                    self.direction = d[0] if self.c_turn == 1 else (d[1] if self.c_turn == 3 else i)
                    break
            self.c_turn = self.c_turn + 1 if self.c_turn < 3 else 1

        self.x, self.y = new_x, new_y

    def __str__(self):
        return cart_symbols[self.direction]

field = Field("input")
speed = 0.1

def main():
    clear()
    print(field)
    # time.sleep(speed)

    while True:
        clear()
        field.tick()
        # time.sleep(speed)

if __name__ == '__main__':
    main()
