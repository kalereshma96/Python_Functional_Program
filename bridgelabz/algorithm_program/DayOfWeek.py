"""

"""

# Import sys
import  sys

# getDay function from Utility
from com.bridgelabz.utility.Utility import Utility


def dayOfWeek():
    utilityObj = Utility()
    print("Enter date in month/day/year format")
    m = int(input("enter month:"))
    d = int( input("enter day:"))
    y = int( input("enter year:"))
    res = utilityObj.getDay(m,d,y)
    day=["sunday", "monday", "tuesday", "wedneday", "thursday","friday","saturaday"]
    print(day[res])


if __name__ in '__main__':
    print("Program execution start")
    dayOfWeek()


