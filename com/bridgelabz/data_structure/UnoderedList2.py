from com.bridgelabz.utility.Data_structure_utility import *

if __name__=="__main__":
    alist = UnorderedList()
    alist.add(40)
    alist.add(63)
    alist.add(37)
    alist.append(105)
    alist.append(103)
    print(alist)
    print(alist.getIndex(27))
    print(alist.getItem(4))
    alist.pop(4)
    print(alist)
    alist.insert(1, 5)
    print(alist)
    # alist.elementPrint()

