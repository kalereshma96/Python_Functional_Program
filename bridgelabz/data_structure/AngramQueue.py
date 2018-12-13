"""
purpose   :Add the Prime Numbers that are Anagram in the Range of 0 - 1000
           in a Queue using the Linked List and Print the Anagrams from the Queue.
@Author   : Reshma Y. Kale

"""
from com.bridgelabz.utility.Data_structure_utility import *
from com.bridgelabz.utility.Utility import Utility

if __name__ == "__main__":
    q = Queue()


    utility_obj = Utility()
    print("Enter the lower limit:")
    lower_limit = utility_obj.inputInteger()
    print("Enter the upper limit:")
    upper_limit = utility_obj.inputInteger()
    upper_limit = utility_obj.inputInteger()
    storeList = utility_obj.getPrime(lower_limit,upper_limit)
    q.anagramQueue(storeList)