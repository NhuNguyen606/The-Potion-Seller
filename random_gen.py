""" RandomGen Class Implementation.

Defines the RandomGen class used to generate random numbers given a seed.
"""

__author__ = "Zhongxun Pan"

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
        self.modulus = pow(randrange(10), randrange(50))
        self.a = 134775813
        self.c = 1
        self.seed = seed

    def randint(self, k: int) -> int:
        """
        Generates a random number from 1 to k inclusive
        Args:
            k: inclusive upper bound for rand number
        :complexity: O(1)
        """
        random_generator = lcg(self.modulus, self.a, self.c, self.seed)
        count = 0
        temp_list = []
        for number in random_generator:
            temp_list.append(format(number, "b")[0:16])
            count += 1
            if count >= 6:
                break
        temp_list.pop(0)
        res = 0
        for _ in temp_list:
            res += int(_)
        output = ""
        for _ in str(res):
            if int(_) >= 3:
                output += "1"
            else:
                output += "0"
        final_generated_random_number = int(output, 2)
        return final_generated_random_number % k + 1
