import unittest

from random_gen import RandomGen

class TestRandom(unittest.TestCase):
    
    def test_run(self):
        r = RandomGen(seed=0)
        self.assertEqual(r.randint(100), 77)
        self.assertEqual(r.randint(100), 30)
        r = RandomGen(seed=25)
        self.assertEqual(r.randint(100), 69)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRandom)
    unittest.TextTestRunner(verbosity=0).run(suite)
