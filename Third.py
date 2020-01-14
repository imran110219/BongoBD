class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def lca(node1, node2):
    if node1 == node2.parent:
        return node1.value
    if node2 == node1.parent:
        return node2.value
    if node1.parent == node2.parent:
        return node1.parent.value
    elif node1.parent.value < node2.parent.value:
        node2 = node2.parent
    elif node1.parent.value > node2.parent.value:
        node1 = node1.parent
    return lca(node1.parent, node2.parent)

root = Node(1, None)
node_2 = Node(2, root)
node_3 = Node(3, root)
node_4 = Node(4, node_2)
node_5 = Node(5, node_2)
node_6 = Node(6, node_3)
node_7 = Node(7, node_3)
node_8 = Node(8, node_4)
node_9 = Node(9, node_4)

print(lca(node_4, node_8))