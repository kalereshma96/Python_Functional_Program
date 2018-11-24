
#Take input $Stake, $Goal and Number of times from
#user

from com.bridgelabz.utility.Utility import Utility

utility_obj = Utility()
stake = int(input("Enter stakes:"))
#stake = utility_obj7.getInput(stake)
goal = int(input("Enter goals:"))
#goal = utility_obj7.getInput(goal)
NoofTimes = int(input("Enter number of times:"))
#NoofTimes = utility_obj7.getInput(NoofTimes)


list = []
list = utility_obj.getInput(stake, goal, NoofTimes)

print("No of wins are:", list[0])
print("Percentage of wins:", list[1])
print(" Percentage of loss:",list[2])
































































































