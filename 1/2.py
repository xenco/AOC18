freq = 0
freqs = set()
data = [int(x) for x in open("input").readlines()]
found = False
while not found:
    for d in data:
        freqs.add(freq)
        freq += d
        found = freq in freqs
        if found: break
print("Found: ", freq)