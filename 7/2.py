from collections import defaultdict

nodes = defaultdict(list)
invertices = defaultdict(int)

with open("input") as f:
    for line in f.readlines():
        nodes[line.split()[1]].append(line.split()[7])
        invertices[line.split()[1]] = 0

path = ""
seconds_total = 0
worker = [{"node": None, "tick": 0, "tick_begin": 0} for x in range(5)]

for node in nodes:
    for n in nodes[node]:
        invertices[n] += 1

print("Second\tWorker 1\tWorker 2\tWorker 3\tWorker 4\tWorker 5\tDone")

node_in_progress = []
while len(nodes) > 0:
    for i, w in enumerate(worker):
        node = sorted([node for node in nodes if invertices[node] == 0 and not node in node_in_progress], key=lambda x: ord(x))
        if (len(node) > 0):
            node = node[0]

            if worker[i]["node"] == None:
                worker[i]["node"] = node

                seconds_for_node = ord(node) - 64 + 60
                worker[i]["tick"] = seconds_for_node
                worker[i]["tick_begin"] = seconds_for_node

                node_in_progress.append(node)

    # tick
    second_added_for_tick = False
    for i, w in enumerate(worker):
        if (worker[i]["node"] != None):
            worker[i]["tick"] -= 1

            if not second_added_for_tick:
                seconds_total += 1
            second_added_for_tick = True

            if worker[i]["tick"] == 0:
                path += worker[i]["node"]
                nodes[worker[i]["node"]] = sorted(nodes[worker[i]["node"]], key=lambda x: ord(x))
                for n in nodes[worker[i]["node"]]:
                    invertices[n] -= 1
                del nodes[worker[i]["node"]]
                del invertices[worker[i]["node"]]
                worker[i]["node"] = None

    if len(nodes) == 0 and len(invertices) > 0:
        for i in invertices:
            nodes[i] = []

    print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t%s" % (
        seconds_total,
        worker[0]["node"] if worker[0]["node"] != None else ".",
        worker[1]["node"] if worker[1]["node"] != None else ".",
        worker[2]["node"] if worker[2]["node"] != None else ".",
        worker[3]["node"] if worker[3]["node"] != None else ".",
        worker[4]["node"] if worker[4]["node"] != None else ".",
        path
    )
          )

print(path)
