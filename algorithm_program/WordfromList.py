from com.bridgelabz.utility.Utility import Utility

utilityObj = Utility()
word_list = int(input("how many words you want to enter:"))
print("Enter list of words")
storeelement=[]
storeelement=utilityObj.getStringElement(word_list)
utilityObj.getWord(storeelement)
