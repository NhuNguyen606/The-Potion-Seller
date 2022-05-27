from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen


class Game:

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.total_potion = None
        self.inventory = []

    def set_total_potion_data(self, potion_data: list) -> None:
        self.total_potion = LinearProbePotionTable(len(potion_data), True)
        for i in potion_data:
            new_potion = Potion.create_empty(i[1], i[0], i[2])
            self.total_potion.insert(new_potion.name, (new_potion.potion_type, new_potion.buy_price))

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        self.inventory = AVLTree()
        for i in potion_name_amount_pairs:
            # Not sure what to put instead of the self.inventory.root
            self.inventory.insert_aux(self.inventory.root, i[0], (i[1], i[2]))

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        raise NotImplementedError()

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        raise NotImplementedError()
