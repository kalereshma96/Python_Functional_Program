"""
purpose   :Take a range of 0 - 1000 Numbers and find the
           Prime numbers in that range. Store the prime
           numbers in a 2D Array.
@Author   : Reshma Y. Kale

"""
from com.bridgelabz.utility.Data_structure_utility import *
from com.bridgelabz.utility.Data_structure_utility import *
utility_obj = Utility()
print("Enter the lower limit:")
lower_limit = utility_obj.inputInteger()
print("Enter the upper limit:")
upper_limit = utility_obj.inputInteger()
primenumber = []
primenumber = utility_obj.getPrime(lower_limit, upper_limit)

Data_structure_obj.primenslots(primenumber)
