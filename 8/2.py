input = open("input").read().split()

class Tree():
    def __init__(self):
        self.root = None

    def build(self, node):
        if self.root == None:
            self.root = node

        for i in range(node.num_children):
            node.addChild(self.build(Node(input.pop(0), input.pop(0))))

        for j in range(node.num_meta):
            node.addMeta(input.pop(0))

        return node


class Node():
    def __init__(self, num_children, num_meta):
        self.num_children = int(num_children)
        self.children = []
        self.num_meta = int(num_meta)
        self.meta = []
        self.sum_meta = 0

    def addChild(self, node):
        self.children.append(node)
        self.num_children = len(self.children)

    def addMeta(self, meta):
        self.meta.append(int(meta))

    def getSumMeta(self):
        sum_m = 0
        if len(self.children) == 0:
            sum_m += sum(self.meta)
        else:
            for m in self.meta:
                if m > 0 and m <= len(self.children):
                    x = self.children[m - 1].getSumMeta()
                    sum_m += x
        return sum_m


tree = Tree()
tree.build(Node(input.pop(0), input.pop(0)))
print(tree.root.getSumMeta())
