#This program takes a command-line argument N and prints
# a table of the powers of 2 that are less than or equal to 2^N.

#import sys
#power = sys.argv[0]
#print(power)
# power = int(input("enter power:"))
# print(power)
# temp = 1
# if power > 31:
#     print("enter value less than 31")
#
# for i in range(1, power):
#     temp = temp * 2
# print(power, "of is", temp)

from com.bridgelabz.utility.Utility import Utility
utility_obj = Utility()
power = int(input("enter power:"))
power = utility_obj.inputPower(power)
#print(power, "of is", temp)


