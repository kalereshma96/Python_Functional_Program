import sys
import math
#print("Enter x :")
x = int( sys.argv[1])
#print("Enter y:")
y = int(sys.argv[2])
val1 =math.pow (x,x)
val2 =math. pow(y,y)
distance = math.sqrt(val1 +val2)
print("distance is", distance)
