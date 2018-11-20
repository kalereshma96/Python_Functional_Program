#Its take year as input and Print the year is a Leap Year or not.

# year = int(input("Enter year to check if it is leap year or not:"))
# # ensureentered year is a 4 digit number
# if year < 4:
#     print("Enter 4 digit number...")
# else:
#     print(year)
#
# if (year % 4 == 0 and year % 400 == 0 and year % 100 == 0):
#     print(year ," is leap year")
# else:
#     print(year, "not a leap year")

from com.bridgelabz.utility.Utility import Utility
utility_obj3 = Utility()
year = int(input("Enter year to check if it is leap year or not:"))
year = utility_obj3.inputYear(year)
