from __future__ import annotations
# ^ In case you aren't on Python 3.10

from random_gen import RandomGen

class Game:
    
    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
    
    def set_total_potion_data(self, potion_data: list) -> None:
        raise NotImplementedError()

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        raise NotImplementedError()

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        raise NotImplementedError()

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        raise NotImplementedError()

