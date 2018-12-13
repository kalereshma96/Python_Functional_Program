#Flip Coin and print percentage of Heads and Tails


#import random
#The number of times to Flip Coin. Ensure it is positive integer.

#flip = int(input("Enter no of flip you want:"))
#print(flip)



#for i in range(0, flip):
# if (flip < 0):
    #print("Enter positive number:")

#Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads

 #   val = random.randint(0, 1)
  #  if(val < 0.5):
   #   tailcount = tailcount + 1
    #else:
     # headcount = headcount + 1

#Percentage of Head and Tails

#per1 = tailcount / flip * 100
#per2 = headcount / flip * 100
#print("Percentage of tails ", per1)
#print("Percentage of heads ", per2)

from com.bridgelabz.utility.Utility import Utility
headcount = 0
tailcount = 0

utility_obj = Utility()
flip = int(input("Enter no of flip you want:"))
print(flip)
flip = utility_obj.inputInt(flip)


