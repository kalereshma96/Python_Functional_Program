
"""
purpose   : Hashing Function to search a Number in a slot
@Author   : Reshma Y. Kale
@version  : 1.0
"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Data_structure_utility import *

if __name__ == "__main__":
    utility = Utility()
    hash = HashFunction()
    storeelement = [40, 45, 11, 42, 85, 10, 67, 55]
    slots = 8
    hashlist = hash.hashFunction(slots, storeelement)
    print(hashlist)
    print("Enter the no you want to search:")
    key = utility.inputIntiger()
    hash.hashSearch(key, hashlist, slots)
