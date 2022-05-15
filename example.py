from game import Game

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

# Now for choosing vendors!
selling = G.choose_potions_for_vendors(4)
print(selling)
# >>> [
#     ("Potion of Extreme Speed", 5), 
#     ("Potion of Increased Stamina", 10),
#     ("Potion of Health Regeneration", 4),
#     ("Potion of Instant Health", 3),
# ]

# Let’s suppose that the adventurers will pay 30, 15, 15, and 20 dollars per litre for each of the potions listed below.
full_vendor_info = [
    ("Potion of Health Regeneration", 30),
    ("Potion of Extreme Speed", 15),
    ("Potion of Instant Health", 15),
    ("Potion of Increased Stamina", 20),
]

# Play the game with 3 attempts, at different starting money.
results = G.solve_game(full_vendor_info, [12.5, 45, 80])
print(results)
# >>> [37.5, 90, 142.5]
