from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen


class Game:

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.total_potions = None
        self.inventory = None

    def set_total_potion_data(self, potion_data: list) -> None:
        """
        Creates hash table to store all possible potions, sets inventory of vendors to contain 0 of each potion
        Args:
            potion_data: List containing all possible potions
        :complexity: O(N*log(N)), where N is the length of potion_data
        """
        self.total_potions = LinearProbePotionTable(len(potion_data))
        self.inventory = AVLTree()
        for i in potion_data:
            new_potion = Potion.create_empty(i[1], i[0], i[2])
            self.total_potions.insert(new_potion.name, (new_potion.potion_type, new_potion.buy_price))
            self.inventory[new_potion.buy_price] = (new_potion.name, 0)

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """
        Adds litres of particular potions into the inventory of vendors
        Args:
            potion_name_amount_pairs: list of tuples containing two elements: The name of the potion, and amount in litres to add
             to the inventory.
        :complexity: O(C*log(N)), where C is the length of potion_name_amount_pairs, and N is the number of potions in
        self.total_potions
        """
        self.inventory = AVLTree()
        for i in potion_name_amount_pairs:
            price = self.total_potions[i[0]][1]
            self.inventory[price] = (i[0], i[1])

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """
        Completes the vendor potion selection process
        Args:
            num_vendors: number of vendors who will sell potions
        :complexity: O(C*log(N)), where C is equal to num_vendors, and N is the number of potions in
        self.total_potions
        """
        output = []
        prices = []
        for i in range(num_vendors):
            potion_stock = len(self.inventory)
            p = self.rand.randint(potion_stock)
            potion = self.inventory.kth_largest(p)
            output.append(potion.item)
            prices.append(potion.key)
            del self.inventory[potion.key]

        for j in range(num_vendors):
            self.inventory[prices[j]] = output[j]

        return output

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        raise NotImplementedError()
