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
"""
purpose   :The deque abstract data type.performs 
           various operations such as add at front,
           add at rear etc.
@Author   : Reshma Y. Kale

"""

from com.bridgelabz.utility.Data_structure_utility import *

dq = Deque()
# dq.addFront(12)
# dq.addRear(9)
# dq.addFront(8)
# dq.addFront(62)
# dq.addRear(45)
#print(dllist.removeRear())
#dllist.removeFront(9,12)
#dq.listprint(dq.head)