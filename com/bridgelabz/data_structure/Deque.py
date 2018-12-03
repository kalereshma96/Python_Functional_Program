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

class Node():
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      self.head = None

class doubly_linked_list:
   def __init__(self):
      self.head = None

#add at beggining
   def addFront(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

#append method to add at end
   def addRear(self, NewVal):

          NewNode = Node(NewVal)
          NewNode.next = None
          if self.head is None:
             NewNode.prev = None
             self.head = NewNode
             return
          last = self.head
          while (last.next is not None):
             last = last.next
          last.next = NewNode
          NewNode.prev = last
          return
 #remove from front
#   def removeFront(self):
 #      return self.head.pop()




  # def removeRear(self):
   #    return self.head.pop(0)

   def removeFront(self,head,data):
       size=0
       val = None
       if (head == None):
           print("No elements to delete")
       else:
          val=head.data
          head=head.next
          size=size-1
          return val



  # Define the method to print

   def listprint(self, node):
       while (node is not None):
           print(node.data),
           last = node
           node = node.next



dllist = doubly_linked_list()
dllist.addFront(12)
dllist.addRear(9)
dllist.addFront(8)
dllist.addFront(62)
dllist.addRear(45)
#print(dllist.removeRear())
#dllist.removeFront(9,12)
dllist.listprint(dllist.head)