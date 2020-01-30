def getFullState(plants, i, plant):
    full_state = ""
    if i == 0:
        full_state += ".."
    elif i == 1:
        full_state += "." + plants[i - 1]
    else:
        full_state +=  plants[i - 2] + plants[i - 1]

    full_state += plant

    if i == len(plants) - 2:
        full_state += plants[i + 1] + "."
    elif i == len(plants) - 1:
        full_state += ".."
    else:
        full_state += plants[i + 1] + plants[i + 2]

    return full_state

plants = []
rules = []

with open("input") as f:
    d = f.readlines()
    plants = "." * 25 + d[0].strip().replace("initial state: ", "") + "." * 25
    rules = [r.strip().replace(" => #", "") for r in d[2:] if r.strip()[-1] == "#"]
    f.close()

print(rules)
print("[0] \t%s" % plants)

num_gen = 20
last_state = []

for i_gen in range(num_gen):
    next_gen = ""
    for i, plant in enumerate(plants):
        fs = getFullState(plants, i, plant)
        has_rule = fs in rules
        next_gen += "#" if has_rule else "."

    plants = next_gen
    last_state = plants
    print("[%s] \t%s" % (i_gen + 1, next_gen))

c = 0
for i,plant in enumerate(last_state):
    if plant == "#":
        real_index = i - 25
        c += real_index
print(c)