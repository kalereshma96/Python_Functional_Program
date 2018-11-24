import  sys
from com.bridgelabz.utility.Utility import Utility
utilityObj = Utility()
print("Enter date in month/day/year format")
m = int( sys.argv[1])
d = int( sys.argv[2])
y = int( sys.argv[3])
utilityObj.getDay(m,d,y)


