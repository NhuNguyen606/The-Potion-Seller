import unittest

from hash_table import LinearProbePotionTable

class TestTable(unittest.TestCase):
    
    def test_tablesize(self):
        c1 = LinearProbePotionTable(100, True, 120)
        c2 = LinearProbePotionTable(100, True, -1)
        # Should be exactly 120.
        self.assertEqual(len(c1.table), 120)
        # Should at least accomodate all positions.
        self.assertGreaterEqual(len(c2.table), 100)
    
    def test_stats(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 5,
            "s2": 5,
            "s3": 5,
            "s4": 7
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved
        
        self.assertEqual(l.statistics(), (3, 4, 2))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTable)
    unittest.TextTestRunner(verbosity=0).run(suite)
