""" RandomGen Class Implementation.

Defines the RandomGen class used to generate random numbers given a seed.
"""

__author__ = "Behnam Mozafari, Zhongxun Pan"

from typing import Generator
from random import randrange


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator.
    :complexity: worst case: O(1)
    """
    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:

    def __init__(self, seed: int = 0) -> None:
        self.random_nums = lcg(pow(2, 32), 134775813, 1, seed)

    def randint(self, k: int) -> int:
        """
        Generates a random number from 1 to k inclusive
        Args:
            k: inclusive upper bound for rand number
        :complexity: O(1)
        """
        temp_list = []
        for number in self.random_nums:
            binary_num = bin(number)
            adjusted_num = int(binary_num[2:])
            if len(binary_num) > 3:
                adjusted_num = int(binary_num[2:len(binary_num) - 16])

            temp_list.append(adjusted_num)

        total = str(sum(temp_list)).zfill(16)
        random_num = ""
        for x in total:
            if int(x) > 2:
                random_num += "1"
            else:
                random_num += "0"

        return int(random_num, 2) % k + 1


