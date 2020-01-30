input = open("input").read().split()

class Tree():
    def __init__(self):
        self.root = None
        self.sum_meta = 0

    def build(self, node):
        if self.root == None:
            self.root = node
        for i in range(node.num_children):
            node.addChild(self.build(Node(input.pop(0), input.pop(0))))
        for j in range(node.num_meta):
            self.sum_meta += node.addMeta(input.pop(0))
        return node

class Node():
    def __init__(self, num_children, num_meta):
        self.num_children = int(num_children)
        self.children = []
        self.num_meta = int(num_meta)
        self.meta = []

    def addChild(self, node):
        self.children.append(node)

    def addMeta(self, meta):
        self.meta.append(int(meta))
        return int(meta)

tree = Tree()
tree.build(Node(input.pop(0), input.pop(0)))
print(tree.sum_meta)
