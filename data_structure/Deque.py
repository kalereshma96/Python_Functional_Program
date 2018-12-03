# class Deque:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
# 	    return self.items == []
#     def addFront(self, item):
# 	    self.items.append(item)
#     def addRear(self, item):
# 	    self.items.insert(0,item)
#     def removeFront(self):
#         return self.items.pop()
#     def removeRear(self):
#         return self.items.pop(0)
#     def size(self):
#         return len(self.items)
#     #def listprint(self, node):
#      #   while (node is not None):
#       #      print(node.items)
#           #  last = node
#            # node = node.next
#
#
# d=Deque()
# print(d.isEmpty())
# #d.addRear('dog')
# d.addRear('lkj')
# d.addFront('cat')
# # d.addFront(True)
# # print(d.size())
# # print(d.isEmpty())
# # d.addRear(8.4)
# # print(d.removeRear())
# # print(d.removeFront())
# #d.listprint(d.items)


from collections import deque

from com.bridgelabz.utility.Data_structure_utility import *

dllist = doubly_linked_list()
dllist.addFront(12)
dllist.addRear(9)
dllist.addFront(8)
dllist.addFront(62)
dllist.addRear(45)
#print(dllist.removeRear())
#dllist.removeFront(9,12)
dllist.listprint(dllist.head)