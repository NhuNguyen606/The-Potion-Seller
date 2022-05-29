from __future__ import annotations
# ^ In case you aren't on Python 3.10
from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen


class Game:
    """

    """
    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed=seed)
        self.total_potions = None
        self.inventory = None
        self.game_potions = None

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
        Optimally purchases potions from vendors to maximise profits
        Args:
            potion_valuations: list of potions that each vendor is selling, paired with its valuation by the adventurers
            starting_money: is a list containing, for each attempt, the starting allowance the player has
        :complexity:
        """
        self.game_potions = AVLTree()
        num_potions = len(potion_valuations)
        # Finds profit for each potion
        potion_profits = LinearProbePotionTable(num_potions)
        for i in potion_valuations:
            buy_price = self.total_potions[i[0]][1]
            profit = i[1] - buy_price
            if profit > 0:
                potion_litres = self.inventory[buy_price][1]
                profit_str = str(profit)
                if profit_str in potion_profits:
                    potion_profits[profit_str] = potion_profits[profit_str]+1
                else:
                    potion_profits[profit_str] = 0
                self.game_potions[profit*num_potions + potion_profits[profit_str]] = (i[0], buy_price, potion_litres, profit)

        output = []

        for j in starting_money:
            total_profit = j
            deleted_potions = []
            while j > 0:
                most_profit = self.game_potions.kth_largest(1)
                profit = most_profit.item[3]
                name = most_profit.item[0]
                buying_price = most_profit.item[1]
                litres = most_profit.item[2]
                # If we can buy all the stock of the most profitable potion
                if litres * buying_price <= j:
                    total_profit += profit * litres
                    deleted_potions.append((most_profit.key, name, buying_price, litres, profit))
                    del self.game_potions[most_profit.key]
                    j -= litres * buying_price
                # We have to buy a certain amount of the most profitable potion
                else:
                    # calculate amount we can buy
                    num_litres = j / buying_price
                    total_profit += num_litres * profit
                    j -= num_litres * buying_price
            output.append(total_profit)
            for k in deleted_potions:
                self.game_potions[k[0]] = (k[1], k[2], k[3], k[4])

        return output
