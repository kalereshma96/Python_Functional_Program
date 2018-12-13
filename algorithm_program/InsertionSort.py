from com.bridgelabz.utility.Utility import Utility

utilityObj = Utility()
s = int(input("enter size:"))
storeelement=[]
print("Enter arrayelement:")
storeelement=utilityObj.getStringElement(s)
utilityObj.getInsertion(storeelement)