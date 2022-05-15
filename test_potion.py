import unittest

from potion import Potion

class TestPotion(unittest.TestCase):
    
    def test_creation(self):
        p = Potion("Buff", "Potion of Extreme Speed", 40, 4)
        self.assertEqual(p.name, "Potion of Extreme Speed")
        self.assertEqual(p.potion_type, "Buff")
        self.assertEqual(p.buy_price, 40)
        self.assertEqual(p.quantity, 4)
        p2 = Potion.create_empty("Health", "Potion of Regeneration", 20)
        self.assertEqual(p2.name, "Potion of Regeneration")
        self.assertEqual(p2.potion_type, "Health")
        self.assertEqual(p2.buy_price, 20)
        self.assertEqual(p2.quantity, 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPotion)
    unittest.TextTestRunner(verbosity=0).run(suite)
