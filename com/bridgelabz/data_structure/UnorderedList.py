
# Additions (Add) grow the list by adding items to the end of the list.
# Removals (Remove) will always remove from a given position in the list.
# Search (Contains) will search the list for a value.

from com.bridgelabz.utility.Utility import Utility

class Node():
    def __init__(self,data=None):
         self.data = data
         self.next = None




class LinkedList():
    def __init__(self):
        self.head = None




   #add element at beginning
    # def Atbeginning(self,newdata):
    #     NewNode = Node(newdata)
    #
    #     NewNode.next= self.head
    #     self.head = Node(newdata)

     #add element at the end
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = newdata
            return
        endElement = self.head
        while (endElement.next):
            endElement = endElement.next
        endElement.next = NewNode

     #inbetween in two nodes
    def AtMid(self,midNode,newdata):
        if midNode is None:
            print("middle node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next=midNode.next
        midNode.next=newdata

    # print element
    # traverse through linkedlist
    def elementPrint(self):
        element=self.head
        while element is not None:
            print(element.data)
            element =element.next



list = LinkedList()
list.head = Node('1')
element2 = Node("abc")
element3 = Node('2')

#assign headnode to next value

list.head.next=element2
element2.next=element3
list.AtEnd("kale")
#list.Atbeginning("reshma")
list.AtMid(list.head.next,"ll")

list.elementPrint()








