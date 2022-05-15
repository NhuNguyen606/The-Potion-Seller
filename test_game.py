import unittest

from game import Game

class TestGame(unittest.TestCase):
    
    def test_choose_vendors(self):
        # Potion names are just numbers here to ensure uniqueness
        g = Game()
        g.set_total_potion_data([
            (str(x), str(x), x)
            for x in range(1, 101)
        ])
        g.add_potions_to_inventory([
            (str(x), x)
            for x in range(2, 101)
        ])
        # Vendor Selection never selects empty potions
        res = g.choose_potions_for_vendors(99)
        self.assertFalse("1" in res)
        # Vendor Selection can be redone - inventory is not changed
        res2 = g.choose_potions_for_vendors(99)
        self.assertTrue(len(res2) == 99)
        # Vendor Selection gives unique results
        self.assertTrue(len(set(res)) == len(set(res2)) == 99)

    def test_example(self):
        G = Game()
        # There are these potions, with these stats, available over the course of the game.
        G.set_total_potion_data([
            # Name, Category, Buying price from vendors.
            ["Potion of Health Regeneration", "Health", 20],
            ["Potion of Extreme Speed", "Buff", 10],
            ["Potion of Deadly Poison", "Damage", 45],
            ["Potion of Instant Health", "Health", 5],
            ["Potion of Increased Stamina", "Buff", 25],
            ["Potion of Untenable Odour", "Damage", 1],
        ])

        # Start of Day 1
        # Let’s begin by adding to the inventory of PotionCorp:
        G.add_potions_to_inventory([
            ("Potion of Health Regeneration", 4),
            ("Potion of Extreme Speed", 5),
            ("Potion of Instant Health", 3),
            ("Potion of Increased Stamina", 10),
            ("Potion of Untenable Odour", 5),
        ])
        
        full_vendor_info = [
            ("Potion of Health Regeneration", 30),
            ("Potion of Extreme Speed", 15),
            ("Potion of Instant Health", 15),
            ("Potion of Increased Stamina", 20),
        ]

        # Play the game with 3 attempts, at different starting money.
        results = G.solve_game(full_vendor_info, [12.5, 45, 80])
        self.assertEqual(results, [37.5, 90, 142.5])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGame)
    unittest.TextTestRunner(verbosity=0).run(suite)
