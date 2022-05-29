""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor, modified by Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from referential_array import ArrayR
from typing import TypeVar, Generic
from primes import largest_prime
from potion import Potion
T = TypeVar('T')


class LinearProbePotionTable(Generic[T]):
    """
    Linear Probe Potion Table

    This potion table does not support deletion.

    attributes:
        count: number of elements in the hash table
        table: used to represent our internal array
        table_size: current size of the hash table
    """

    def __init__(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        # Statistic setting
        self.conflict_count = 0
        self.probe_max = 0
        self.probe_total = 0
        if tablesize_override == -1:
            self.tablesize = largest_prime(3 * max_potions)
        else:
            self.tablesize = tablesize_override
        self.initalise_with_tablesize(self.tablesize)
        self.good_hash = good_hash

    def hash(self, potion_name: str) -> int:
        """
        Hashes a potion name using either good_hash or bad_hash
        :param potion_name: Name of potion to be hashed
        :complexity best: O(1)
        :complexity worst: O(n)
        """
        if self.good_hash:
            return Potion.good_hash(potion_name, self.tablesize)
        else:
            return Potion.bad_hash(potion_name, self.tablesize)


    def statistics(self) -> tuple:
        """
        Return the statistics of potion table: conflict_count, probe_total and probe_max
        """
        return self.conflict_count, self.probe_total, self.probe_max

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    def __linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        :complexity best: O(K) first position is empty
                          where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash

        conflict = False
        probes = 0

        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    if conflict:
                        self.conflict_count += 1
                        if probes > self.probe_max:
                            self.probe_max = probes
                        self.probe_total += probes
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                if conflict and is_insert:
                    self.conflict_count += 1
                    if probes > self.probe_max:
                        self.probe_max = probes
                    self.probe_total += probes
                return position
            else:  # there is something but not the key, try next
                conflict = True
                probes += 1
                position = (position + 1) % len(self.table)

        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :raises KeyError: when the item doesn't exist
        """
        position = self.__linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set a (key, data) pair in our hash table
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        if len(self) == len(self.table) and key not in self:
            raise ValueError("Cannot insert into a full table.")
        position = self.__linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1
        self.table[position] = (key, data)

    def initalise_with_tablesize(self, tablesize: int) -> None:
        """
        Initialise a new array, with table size given by tablesize.
        Complexity: O(n), where n is len(tablesize)
        """
        self.count = 0
        self.table = ArrayR(tablesize)

    def is_empty(self):
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
        Returns whether the hash table is full
        :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result


if __name__ == '__main__':
    hash_names = ["healing", "health", "strength", "damage", "odour", "stamina", "speed", "armour", "behnam", "tiger", "sleeping"]
    test_table = LinearProbePotionTable(11, False)
    test_table_good = LinearProbePotionTable(11)
    for i in hash_names:
        test_table.insert(i, i)
        test_table_good.insert(i, i)
    print(test_table_good.statistics())
    print(test_table.statistics())

    dataset = ["Italy", "Israel", "Australia", "Auckland", "America", "Argentina", "Iceland", "India", "Ireland", "Indonesia"]
    dataset_table_good = LinearProbePotionTable(len(dataset))
    dataset_table_bad = LinearProbePotionTable(len(dataset), False)
    for data in dataset:
        dataset_table_good.insert(data, data)
        dataset_table_bad.insert(data, data)
    print(dataset_table_good.statistics())
    print(dataset_table_bad.statistics())

    cities = ["Mumbai", "Melbourne", "Mexico City", "Moscow", "Madrid", "Mogadishu", "Mashhad", "Maracaibo", "Medellin", "Maracay", "Medan"]
    cities_good_hash = LinearProbePotionTable(len(cities))
    cities_bad_hash = LinearProbePotionTable(len(cities), False)
    for city in cities:
        cities_good_hash.insert(city, city)
        cities_bad_hash.insert(city, city)
    print(cities_good_hash.statistics())
    print(cities_bad_hash.statistics())
