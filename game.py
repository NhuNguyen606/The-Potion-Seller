from __future__ import annotations
# ^ In case you aren't on Python 3.10

from random_gen import RandomGen

class Game:
    
    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
    
    def set_total_potion_data(self, potion_data: list) -> None:
        potion_data.append(["Health", "Potion of Health Regeneration", 20])
        potion_data.append(["Buff", "Potion of Extreme Speed", 10])
        potion_data.append(["Damage", "Potion of Deadly Poison", 45])
        potion_data.append(["Healing", "Potion of Instant Health", 5])
        potion_data.append(["Buff", "Potion of Increased Stamina", 25])
        potion_data.append(["Damage", "Potion of Untenable Odour ", 1])

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        potion_name_amount_pairs.append(("Potion of Health Regeneration", 4))
        potion_name_amount_pairs.append(("Potion of Extreme Speed", 5))
        potion_name_amount_pairs.append(("Potion of Deadly Poison", 0))
        potion_name_amount_pairs.append(("Potion of Instant Health", 3))
        potion_name_amount_pairs.append(("Potion of Increased Stamina", 10))
        potion_name_amount_pairs.append(("Potion of Untenable Odour", 5))



    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        raise NotImplementedError()

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        raise NotImplementedError()

