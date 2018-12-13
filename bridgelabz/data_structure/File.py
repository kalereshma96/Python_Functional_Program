from com.bridgelabz.utility.Data_structure_utility import *
utilityObj = Utility()
s = int(input("enter size:"))
storeelement=[]
print("Enter arrayelement:")
storeelement=utilityObj.getStringElement(s)
def getStringElement(self, s):

    newlist = []
    for i in range(s):
        num = input("")
        newlist.append(num)
    return newlist
    for i in range(0,len(storeelement)):
        print(storeelement[i])
        file = open("example.txt", "w")
        file.write(str(storeelement))
        file.close()
        file = open("example.txt","r")
        if file.mode == 'r':
            contents = file.read()
            print(contents)