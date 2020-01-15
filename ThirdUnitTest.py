import unittest
from Third import lca, Node

class ThreeUnitTest(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(1, None)
        self.node_2 = Node(2, self.node_1)
        self.node_3 = Node(3, self.node_1)
        self.node_4 = Node(4, self.node_2)
        self.node_5 = Node(5, self.node_2)
        self.node_6 = Node(6, self.node_3)
        self.node_7 = Node(7, self.node_3)
        self.node_8 = Node(8, self.node_4)
        self.node_9 = Node(9, self.node_4)

    def test1(self):
        self.assertEqual(lca(self.node_4, self.node_8), 4)

    def test2(self):
        self.assertEqual(lca(self.node_4, self.node_7), 1)

    def test3(self):
        self.assertEqual(lca(self.node_9, self.node_8), 4)


if __name__ == '__main__':
    unittest.main()