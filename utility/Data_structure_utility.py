from collections import deque
###################################Data Stucture###################



class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


###############################################################################
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        list_str = "head"
        current = self.head
        while current != None:
            list_str = list_str + " " + str(current.getData())
            current = current.getNext()
        list_str = list_str + " " + str(None)
        return list_str

    def append(self, item):
        """add items into the linked list"""
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)

    def getIndex(self, item):
        """get the index of an item, assume the first one (head pointing to) is 0"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def getItem(self, index):
        """return an item given an index"""
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise ("index out of range")

    def pop(self, index):
        self.remove(self.getItem(index))

    def insert(self, index, item):
        """insert an item after index item"""
        current = self.head
        for i in range(index):
            current = current.getNext()

        if current != None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise ("index out of range")
    # def elementPrint(self):
    #     current=self.head
    #     while current is not None:
    #        # print(current.head)
    #         current =current.getNext()



############################ Orderd List ##################################3
class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        stop = False
        while not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        list_str = "head"
        current = self.head
        while current != None:
            list_str = list_str +  " " + str(current.getData())
            current = current.getNext()
        list_str = list_str +  " " + str(None)
        return list_str

    def getIndex(self, item):
        """get the index of an item"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def getItem(self, index):
        """return an item given an index"""
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise("index out of range")


    def pop(self, index="Last"):
        if index != "Last":
            self.remove(self.getItem(index))
        else:
            index = self.size() - 1
            self.remove(self.getItem(index))


    def insert(self, index, item):
        """insert an item after index item"""
        current = self.head
        for i in range(index):
            current = current.getNext()

        if current != None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
        else:
            raise("index out of range")

########################## Stack #################################
class Stack():
    top = -1
    stack = []
    def push(self,top,x,n):
        if self.top == n - 1:#initially stack is full
            print("Stack is full..overflow condition..")
        else:
            top = +1
            self.stack[top]= x
    def isEmpty(self):
        if self.top == -1:
            return  True
        else:
            return  False

    def pop(self):
        if self.top == -1:
            print("stack is empty....underflow condition")
        else:
            top = self.top-1
    def size(self):
        return self.top+1
    def peek(self): #return top element of stack
        return self.stack[self.top]
#################### Queue ###################################3
class Queue():
    count = 0
    def construct(self):

        self.queue=list
        self.size=150
        self.rear=0
        self.front=0

    def enqueue(self, data):
        rear=0
        if(self.rear < self.size):
            self.queue[self.rear]=data
            rear = rear + 1
            return self.rear
        else:
            print("queue is full")


    def deque(self):
        if(self.front<self.size):
            self.queue.pop()
            return (self.queue)


    def isEmpty(self):
        if(count(self.queue)==0):
            return True
        else:
            return False

    def sizeOfQue(self):
        result= self.rear - self.front
        return result

    def removeFirst(self):

       x=self.front

################### Deque Node ##########################3
from collections import deque
# pre = None
# data = None
# deque = next
# deque = pre
# deque = data
def Deque(self):
    self.next = None
    self.pre = None
def Deque(self,value):
    self.data = value
    self.next = None
    self.pre = None
####################### DEQUE ################################













