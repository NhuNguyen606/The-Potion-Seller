""" Array-based implementation of List ADT. """

from referential_array import ArrayR
from abstract_list import List, T

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class ArrayList(List[T]):
    """ List ADT implemented with arrays. """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ ArrayList object initialiser. """

        # first, calling the basic initialiser
        super(ArrayList, self).__init__()

        # initialising the internal array
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def reset(self):
        """ Reset the list. """
        List.__init__(self)

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Magic method. Insert the item at a given position. """
        self.array[index] = value

    def __contains__(self, item):
        """ Checks if item is in the list. """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def __shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def __shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        if len(self) < 0:
            raise Exception('Out of bounds')
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def __resize(self) -> None:
        """ Resize the list. """
        # doubling the size of our list
        new_array = ArrayR(2 * len(self.array))

        # copying the contents
        for i in range(self.length):
            new_array[i] = self.array[i]

        # referring to the new array
        self.array = new_array

    def append(self, item: T) -> None:
        """ Append a new item to the end of the list. """
        if self.is_full():
            self.__resize()
        self.array[len(self)] = item
        self.length += 1

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        if self.is_full():
            self.__resize()
        self.__shuffle_right(index)
        self.array[index] = item
        self.length += 1

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        if index < 0 or index > len(self):
            raise IndexError('Out of bounds')
        item = self.array[index]
        self.length -= 1
        self.__shuffle_left(index)
        return item

    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        for i in range(len(self)):
            if item == self.array[i]:
                return i
        raise ValueError('item not in list')

    def is_full(self):
        """ Check if the list is full. """
        return len(self) >= len(self.array)

    def remove(self, item: T) -> None:
        """ Remove an item from the list. """
        index = self.index(item)
        self.delete_at_index(index)
