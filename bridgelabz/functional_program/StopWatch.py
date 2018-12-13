#Stopwatch Program for measuring the time that elapses between the start and end clicks

from com.bridgelabz.utility.Utility import Utility


utility_obj = Utility()
starttime = int(input("press any key to start stopwatch..."))
ss = utility_obj.getStart()
print("start time is:",ss)
stoptime = int(input("Press any key to stop watch.."))
st = utility_obj.getStop()
print("Stop time is:",st)
print("elapsed time is:",starttime - stoptime )
