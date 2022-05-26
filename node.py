""" Implementation of a node in linked lists and binary search trees. """

from typing import TypeVar, Generic

I = TypeVar('I')
K = TypeVar('K')
T = TypeVar('T')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'


class ListNode(Generic[T]):
    """ Simple linked node. It contains an item and has a reference to next node. """

    def __init__(self, item: T = None) -> None:
        """ Node initialiser. """
        self.item = item
        self.next = None

class TreeNode(Generic[K, I]):
    """ Node class represent BST nodes. """

    def __init__(self, key: K, item: I = None) -> None:
        """
            Initialises the node with a key and optional item
            and sets the left and right pointers to None
            :complexity: O(1)
        """
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        """
            Returns the string representation of a node
            :complexity: O(N) where N is the size of the item
        """
        key = str(self.key) if type(self.key) != str else "'{0}'".format(self.key)
        item = str(self.item) if type(self.item) != str else "'{0}'".format(self.item)
        return '({0}, {1})'.format(key, item)

class AVLTreeNode(TreeNode, Generic[K, I]):
    """ Node class for AVL trees.
        Objects of this class have an additional variable - height.
    """

    def __init__(self, key: K, item: I = None) -> None:
        """
            Initialises the node with a key and optional item
            and sets the left and right pointers to None
            :complexity: O(1)
        """

        super(AVLTreeNode, self).__init__(key, item)
        self.height = 1
        self.sub_length = 1
