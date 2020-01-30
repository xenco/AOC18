from collections import defaultdict

nodes = defaultdict(list)
invertices = defaultdict(int)

with open("input") as f:
    for line in f.readlines():
        nodes[line.split()[1]].append(line.split()[7])
        invertices[line.split()[1]] = 0

path = ""
for node in nodes:
    for n in nodes[node]:
        invertices[n] += 1

while len(nodes) > 0:
    node = sorted([node for node in nodes if invertices[node] == 0], key=lambda x: ord(x))[0]
    path += node
    nodes[node] = sorted(nodes[node], key=lambda x: ord(x))
    for n in nodes[node]:
        invertices[n] -= 1
    del nodes[node]
    del invertices[node]

    if len(nodes) == 0 and len(invertices) > 0:
        for i in invertices:
            nodes[i] = []

print(path)
