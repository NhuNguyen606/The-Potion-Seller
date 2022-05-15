import unittest

from bst import BinarySearchTree

class TestBST(unittest.TestCase):
    
    def setUp(self) -> None:
        self.b = BinarySearchTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        self.b.draw()
        """
        15
        ╟─10
        ║ ╟─5
        ║ ║ ╟─3
        ║ ║ ║ ╟─
        ║ ║ ║ ╙─4
        ║ ║ ╙─
        ║ ╙─
        ╙─20
          ╟─17
          ╙─22
        """

        return super().setUp()
    
    def test_minimal(self):
        self.assertEqual(self.b.get_minimal(self.b.get_tree_node_by_key(15)).item, "F")
        self.assertEqual(self.b.get_minimal(self.b.get_tree_node_by_key(20)).item, "D")
    
    def test_successor(self):
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(15)).item, "D")
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(5)), None)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
    unittest.TextTestRunner(verbosity=0).run(suite)
