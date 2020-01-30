import time

input = "320851"
state = "37"
elves = [0, 1]

start = time.time()

while not input in state[-7:]:
    state += str(int(state[elves[0]]) + int(state[elves[1]]))
    elves[0] = (elves[0] + 1 + int(state[elves[0]])) % len(state)
    elves[1] = (elves[1] + 1 + int(state[elves[1]])) % len(state)

print(state.index(input))
print("Duration: %ss" % (time.time() - start))
