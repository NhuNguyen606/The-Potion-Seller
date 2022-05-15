import unittest

from avl import AVLTree

class TestAVL(unittest.TestCase):
    
    def test_run_through(self):
        self.b = AVLTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        # self.b.draw()
        """
        15
        ╟─5
        ║ ╟─3
        ║ ║ ╟─
        ║ ║ ╙─4
        ║ ╙─10
        ╙─20
          ╟─17
          ╙─22
        """
        self.assertEqual(self.b.root.item, "A")
        self.assertEqual(self.b.root.left.left.item, "F")
        self.assertEqual(self.b.root.right.left.item, "D")
        self.assertEqual(self.b.root.left.right.item, "B")
        
        del self.b[20]
        del self.b[17]
        
        # self.b.draw()
        """
        5
        ╟─3
        ║ ╟─
        ║ ╙─4
        ╙─15
          ╟─10
          ╙─22
        """
        self.assertEqual(self.b.root.item, "E")
        self.assertEqual(self.b.root.right.left.item, "B")
        self.assertEqual(self.b.root.left.item, "F")

    def test_kth(self):
        self.b = AVLTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        self.assertEqual([self.b.kth_largest(x).key for x in range(1, 9)], [22, 20, 17, 15, 10, 5, 4, 3])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAVL)
    unittest.TextTestRunner(verbosity=0).run(suite)
