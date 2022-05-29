""" Potion class
    Keep track of potion of the game and create potion objects
"""
class Potion:
    
    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        """
        Constructor to initialise values
            Args:
                potion_type: the type of potion sold
                name: name of potion specifying the exact effects
                buy_price: the amount paid per litre, to purchase this potion from a vendor
                quantity: the amount added to the inventory of the vendors by PotionCorp
            :complexity: O(1)
        """
        self.potion_type = potion_type
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity


    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> 'Potion':
        """
        Create_empty method
        Args:
            potion_type: the type of potion sold
            name: name of potion specifying the exact effects
            buy_price: the amount paid per litre, to purchase this potion from a vendor

        Returns: creates combinations of potion with 0 quantity but different potion_type, name and buy price
        :complexity: O(1)
        """
        return Potion(potion_type, name, buy_price,  0)


    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Good hash method
        This function will be much more effective at avoiding conflicts as we have considered every character in the
        string and also the index of it. Taking into consideration that, we also multiply the base value 'a' each
        time by another number 'b' (of which both are co-prime). Therefore, the base value would change randomly
        each time. Thus, the conflicts and collisions would be deducted efficiently
        Args:
            potion_name: name of potion specifying the exact effects
            tablesize: hash function table size

        Returns: Create a hashing table that is unlikely to create conflicts or collisions
        :complexity: O(n)
        """
        value = 0
        a = 31397
        b = 27179
        for char in potion_name:
            value = (ord(char) + a * value) % tablesize
            a = a * b % (tablesize - 1)
        return value


    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Bad hash method:
        Convert the first character into number, then divide by tablesize and get the reminder. That reminder get hash
        into the hash table
        Args:
            potion_name: name of potion specifying the exact effects
            tablesize: hash function table size

        Returns: Create a hashing table that is likely to create conflicts or collisions
        :complexity: O(1)
        """
        return ord(potion_name[0]) % tablesize








