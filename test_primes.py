import unittest

from primes import largest_prime

class TestPrimes(unittest.TestCase):
    
    def test_some_values(self):
        inputs = [3, 20, 47]
        outputs = [2, 19, 43]
        for i, o in zip(inputs, outputs):
            self.assertEqual(largest_prime(i), o)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimes)
    unittest.TextTestRunner(verbosity=0).run(suite)
