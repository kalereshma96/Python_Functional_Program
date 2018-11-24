from com.bridgelabz.utility.Utility import Utility

import sys

utility_obj = Utility()
t = int(sys.argv[1])
v = int(sys.argv[2])
#t =int(input("enter t"))
#v=int(input("enter v"))

utility_obj.getWindchill(t,v)