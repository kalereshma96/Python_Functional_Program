from com.bridgelabz.utility.Data_structure_utility import *

if __name__=="__main__":

        list = OrderedList()
        list.add(30)
        list.add(31)
        list.add(27)
        list.add(100)
        list.add(101)
        print (list)
        print (list.getIndex(27))
        print (list.getItem(4))
        list.pop(4)
        print (list)
        list.insert(1, 5)
        print (list)