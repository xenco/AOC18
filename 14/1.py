#!/usr/bin/python
from blist import blist

state = blist([3, 7])
elves = [0, 1]

num_iterations = 320851

while len(state) < num_iterations + 10:
    state += [int(c) for c in str(state[elves[0]] + state[elves[1]])]

    for i in range(len(elves)):
        elves[i] = (elves[i] + 1 + state[elves[i]]) % len(state)

result = ''.join([str(state[i]) for i in range(num_iterations, num_iterations + 10)])

print(result)
