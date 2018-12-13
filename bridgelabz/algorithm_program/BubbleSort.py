from com.bridgelabz.utility.Utility import Utility

utilityObj = Utility()
s = int(input("enter array size:"))
storeelement=[]
print("Enter array element:")
storeelement=utilityObj.getIntElement(s)
utilityObj.getBubble(storeelement)