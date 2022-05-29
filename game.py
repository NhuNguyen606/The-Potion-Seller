""" Game Class Implementation.

Defines the Game class used to play the game.
"""

__author__ = "Behnam Mozafari, Zhongxun Pan, Nhu Nguyen"

from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen
from array_sorted_list import ArraySortedList


class Game:
    """
    A hash table is used within the class to hold the total potion data, as each potion has a unique name that can be
    used as a key. Further, the hash table allows for constant time accessing, thus resulting in the fastest way to
    access potion data given the name
    An AVL tree is used for the inventory of vendors, as the prices of potions are unique, thus can be used as keys.
    Further, the AVL tree allows for log(N) time to find the kth largest element,
    thus reducing the choose_potions_for_vendors method's complexity
    A sorted list is used to hold the potion valuation information in the solve_game function, as it was needed to sort
    the potions based on a profit ratio and the sorted list allows for constant time to access its largest element if
    the length is known.
    """

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.total_potions = None
        self.inventory = None

    def set_total_potion_data(self, potion_data: list) -> None:
        """
        Creates hash table to store all possible potions, sets inventory of vendors to contain 0 of each potion
        Args:
            potion_data: List containing all possible potions
        :complexity: worst case: O(N*log(N)), where N is the length of potion_data
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
            potion_name_amount_pairs: list of tuples containing two elements: The name of the potion, and amount in
            litres to add to the inventory.
        :complexity: worst case: O(C*log(N)), where C is the length of potion_name_amount_pairs, and N is the number of
        potions in self.total_potions. This is because the method has a loop which iterates over each element in
        potion_name_amount_pairs and in the loop, each element is inserted into the AVL tree, which takes O(log(N)) time
        thus resulting in a complexity of O(C*log(N)) time.
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
        :complexity: worst case: O(C*log(N)), where C is equal to num_vendors, and N is the number of potions in
        self.inventory. This is because the method contains a loop which iterates C times, where C is the
        num_vendors and within the loop calls the kth_largest function, which has a complexity of O(log(N)), where N is
        the number of potions in the AVL tree.
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
        """
        Plays game. Optimally purchases potions from vendors to maximise profits
        Args:
            potion_valuations: list of potions that each vendor is selling, paired with its valuation by the adventurers
            starting_money: is a list containing, for each attempt, the starting allowance the player has
        :complexity: worst case: O(N*log(N) + M*N), Where N is the length of potion_valuations, and M is the length of
        starting_money. This is because the method contains a loop which iterates over all items in potion_valuations
        (N times), and for each item, performs a get function from an AVL and adds to a sorted list, taking log(N) time,
        thus the first loop has time complexity of O(N*log(N). The second loop iterates over all items in starting_money
        taking M time, and contains a nested loop which has a worst case of iterating over all items in
        potion_valuations, thus taking N time, thus the second loop has a complexity of O(M*N), giving a total
        complexity of O(N*log(N) + M*N).
        """
        num_potions = len(potion_valuations)
        game_potions = ArraySortedList(num_potions)
        # Finds profit for each potion, adding to sorted list
        for i in potion_valuations:
            buy_price = self.total_potions[i[0]][1]
            profit_ratio = i[1] / buy_price
            if profit_ratio > 1:
                potion_litres = self.inventory[buy_price][1]
                game_potions.add((profit_ratio, buy_price, potion_litres))

        output = []

        # keeps on buying and selling most profitable potion
        for j in starting_money:
            total_profit = 0
            k = len(game_potions) - 1
            while j > 0:
                current = game_potions[k]
                profit_ratio = current[0]
                buying_price = current[1]
                litres = current[2]
                # If we can buy all the stock of the most profitable potion, buy it all
                if litres * buying_price <= j:
                    total_profit += profit_ratio * buying_price * litres
                    j -= litres * buying_price
                # We have to buy a certain amount of the most profitable potion
                else:
                    # calculate amount we can buy
                    num_litres = j / buying_price
                    total_profit += profit_ratio * buying_price * num_litres
                    j -= num_litres * buying_price
                k -= 1
            output.append(total_profit)

        return output
