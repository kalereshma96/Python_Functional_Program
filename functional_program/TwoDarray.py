#Two dimensional array is an array within an array.
#  It is an array of arrays. In this type of array the position of an
#  data element is referred by two indices instead of one.
# So it represents a table with rows an dcolumns of data.
from com.bridgelabz.utility.Utility import Utility

utility_obj = Utility()
n = int(input("Enter rows:"))
m = int(input("Enter coluns:"))

utility_obj.getArray(n,m)

