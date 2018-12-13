from collections import deque
from com.bridgelabz.utility.Utility import Utility
utility_obj = Utility()

class Data_structure:


    def inputInteger(self):
        """
         Take a number as input.
        :return: number
        """
        return int(input(""))

    def inputString(self):
        str1 = input(" ")
        return str1

    def primenslots(self, primenumber):
        row = 10
        column = 24
        # list of list to store prime number in slots of 100
        matrix = [[0 for j in range(column)] for i in range(row)]

        rowlist = []
        k = 0
        j = 0

        count = 0
        r = 100
        for i in range(row):
            # rowlist.clear()

            for j in range(column):

                if k < len(primenumber):
                    # to create slots of prime between 100,200 so on
                    if primenumber[k] <= r:
                        matrix[i][j] = primenumber[k]
                        k = k + 1
                    # count=count+1

            r = r + 100
       # print(matrix)

        print("Two D matrix of prime number:")
        for row in matrix:
            for element in row:
                if element != 0:
                    # print prime numbers in matrix format
                    print(element, end=" ")

            print()




Data_structure_obj = Data_structure()
##########################################################################
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
        """
         tests to see whether the list is empty
        :return:
        """
        return self.head == None

    def add(self, item):
        """
         add the new item to the list
        :param item:return nothing
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """

        :return: size of list
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        """
         searches for the item in the list
        :param item:
        :return: return boolean value
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """
         remove item from list

        :param item:
        """
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
        """
                 tests to see whether the list is empty
                :return:
        """
        return self.head == None

    def add(self,item):
        """
        add the new item to the list
        :param item:return nothing
        """
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
        """

        :return: size of the list
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        """
         searches for the item in the list
        :param item:
        :return: return boolean value
        """
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
        """

        :param item: remove item from list
        """
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

    def searchFromFile(self):
        """
        This function read the data from file and store it on linked list.
        user will enter the element to search if it is present in linked list
        then that element is poped from list else element is added on list
        """
        file = open("Wordfile.txt", "w+")  # create file object for read write operation
        list = ["reshma","hrishikesh","suryawanshi"]
        file.writelines(list)  # write data on file
        file.close()  # close file

        file= open("inputword.txt", "r")  # open file for reading data

        filecontent = file.read()
        filecontent = str(filecontent).split()
        # print(Filecontent)
        file.close()

        for i in range(len(list)):
            ol.add(list[i])



        key = input("Enter the Element you want to search:")
        result = ol.search(key)
        print(result)

        if result == False:
            ol.add(key)
        else:
            ol.pop(key)


ol = OrderedList()

########################## Stack #################################
class Stack():
    # top = -1
    # stackSize =15
    # def __init__(self):
    #     self.stack =list ()
    # def push(self,data):
    #     if len(self.stack) > self.stackSize:#initially stack is full
    #         print("Stack is full..overflow condition..")
    #     else:
    #         top = +1
    #         self.stack.insert(top, data) #insert data on top
    #
    #         #self.stack[top]= x
    # def isEmpty(self):
    #     if self.top == -1:
    #         return  True
    #     else:
    #         return  False
    #
    # def pop(self):
    #     if self.top == -1:
    #         print("stack is empty....underflow condition")
    #     else:
    #         top = self.top
    #         temp = self.stack[top]
    #         self.stack.pop()
    #         top -= 1
    #         return temp
    #        # top = self.top-1
    # def size(self):
    #     return self.top+1
    top = 0
    stackMaxsize = 10

    def __init__(self):

        self.stack = list()

    def push(self, data):
        """
        This function is to push element on stack
        :param data: is the data user want to insert
        """
        if len(self.stack) > self.stackMaxsize:  # check for overflow condtion of stack
            print("Overflow!!! no enough space ")
        else:
            tp = self.top
            tp += 1  # increment top
            self.stack.insert(tp, data)  # insert data on top
            # self.stack[tp]=data

    def pop(self):
        """
        This function is to pop data from stack
        :return: topmost element on stack
        """
        if self.stack == []:  # check if stack is empty
            print("Underflow!!! no items in stack")
        else:  # else pop the topmost element from stack
            tp = self.top
            temp = self.stack[tp]
            self.stack.pop()
            tp -= 1
            return temp

    def isEmpty(self):
        """
         This function is to check stack is empty or not
        :return: true if stack is empty else return false
        """
        if self.stack == []:
            return True

    def display(self):
        print(self.stack)

    def size(self):
        return self.top+1

    def peek(self): #return top element of stack
        return self.stack[self.top]

    def balanceParentheses(self):
        """
               Thisfunction is to check the given expression is having balance
               parantheses or not
              """

        string = input("Enter Expression:")
        for i in range(len(string)):
            if string[i] == '(' or i == '[' or i == '{':  # push every occurance of '(' on stack
                st.push(i)

            if ((st.peek() == '(' and i == ')') or (st.peek() == '[' and i == ']') or
                (  st.peek() == '{' and i == '}')) and st.size() > 0:
                    st.pop()
                    continue


            if string[i] == ')' or i == ']' or i == '}': # pop from stack when there occurance of ')'
                        st.pop()


        if st.size()== 0:
            print("Expression is balanced..!!!")
        else:
            print("expression is not balanced..!!")

    def anagram_stack(self, storePrime):
        """
        This method is used to print prime anagram in reverse order.
        :return: nothing
        """
        for i in utility_obj.checkAnagram(storePrime):
            st.push(i)

        for i in range(0, st.size()):
            print(st.pop())
st = Stack()
#################### Queue ###################################3
count = 0
class Queue():
    def construct(self):

        self.queue=list()
        self.size=150
        self.rear=0
        self.front=0

    def enqueue(self, data):
        """
         add a new item at rear of queue
        :param data:
        :return:nothing
        """
        rear=0
        if(self.rear < self.size):
            self.queue[self.rear]=data
            rear = rear + 1
            return self.rear
        else:
            print("queue is full")

    def deque(self):
        """
          remove front item from queue
        :return:
        """
        if(self.front<self.size):
            self.queue.pop()
            return (self.queue)

    def isEmpty(self):
        """
         check whether queue is empty or not
        :return: True or false
        """
        if(count(self.queue)==0):
            return True
        else:
            return False

    def sizeOfQue(self,rear):
        """
        :param rear:
        :return: return the size of queue
        """
        result= self.rear - self.front
        return result

    def removeFirst(self):

       x=self.front



    def bankCounter(self):
        flag = True
        count = 0
        balance=1000
        persons=(int(input("No.of persons:")))
        while count<persons:
            print("Banking cash counter:")
            print("1.Deposite:")
            print("2.Withdraw:")
            print("3.Check current balance:")
            print("4.No of persons in queue:")
            print("Enter your choice...")

            flag = True
            choice = int(input(" "))
            if choice == 1:
                self.deposite()
            if choice == 2:
                self.withdraw()
            if choice == 3:
                self.current_balance(balance)
            if choice == 4:
                self.persons_in_queue(persons)
                while (flag == True):
                    count = count + 1
            print("Do you want to continue transaction...")
            print("Press True or false..")

    def deposit(self):
        """
         In this method people can come in and deposite
         the cash.
        """
        amount = int(input("Enter amount to be deposite."))
        balance=+ amount
        q.enqueue(balance)
        print("Balance is",balance)

    def withdraw(self,balance):
        """

        :param balance:
        """
        withdrawal = int(input("Enter amount to be withdraw."))
        if(withdrawal < balance):
            q.deque()
            bal = balance - withdrawal
            balance = balance - withdrawal
            print("Balance is ", balance)
        else:
            print("Insufficient balance..")

    def current_balance(self,balance):
        """
         It returns the current balance.
        :param balance: current balance
        """
        print("Current balance is",balance)

    def persons_in_queue(self,persons):
       number = q.sizeOfQue(persons)
       print("Number of persons in queue",number)




    def anagramQueue(self, storeList):
        """
        This method is used to print prime anagram using queue.
        :return:
        """

        for i in utility_obj.checkAnagram(storeList):
            q.enqueue(i)

        for i in range(0, q.size()):
            print(q.dequeue())

q = Queue()

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
class Deque():
    # front = None
    # rear = None

    def __init__(self, front=None, rear=None):
        """
        This is the constructor of Deque class.
        :param front: this will always point to first node in the deque
        :param rear: this will always point to last node in the Deque
        """
        #front=None
        #rear=None
        self.front = front
        self.rear = rear

    def addFront(self, data):
        """
        This method is used to insert data at front in Deque.
        :param data: data will be given by user that which data to be inserted in Deque
        :return: nothing
        """
        node = Node(data)
        if self.front == None and self.rear == None:
            self.front = node
            self.rear = node

        else:
            node.next = self.front
            self.front = node

    def addRear(self, data):
        """
        This method is used to insert data at last in Deque.
        :param data:data will be given by user
        :return: nothing
        """

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def show(self):
        """
        This method is used to display content of deque.
        :return:nothing
        """

        if self.front == None:
            print("Queue  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def removeFront(self):
        """
        This is used to remove data which is at front in deque.
        :return:this will return the data which will be removed from the deque
        """

        if self.front.next is None:
            temp = self.front
            self.front = None
            return temp.data

        temp = self.front
        self.front = self.front.next
        return temp.data

    def removeRear(self):
        """
       This is used to remove data which is at rear position in deque.
       :return:this will return the data which will be removed from the deque
       """

        traverse = self.front
        if self.rear == self.front:
            self.rear = None
            self.front = None
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next

        rear_value = self.rear
        self.rear = traverse
        traverse.next = None
        return rear_value.data

    def isEmpty(self):
        """
        This method is used to know whether Deque is empty or not.
        :return:this will return True if Deque is empty or else  return False.
        """

        if self.front == None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to calculate size of Deque
        :return: this will return size of Deque
        """

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size

    def palindrom(self):
        flag = True
        string = (input("Enter String.."))
        for i in range(len(string)):
             str1 = string[i]
             dq.addRear(str1)
             strList = []
             strList = str1
             #print(strList)
             while (dq.size() > 1):
                 if (dq.removeFront() != dq.removeRear()):

                    flag = False
                    break
        if (flag == True):
           print("Enter string is palindrome..")
        else:
           print("Enter string is not palindrome...")

dq = Deque()

####################################################################
class HashFunction:
    def hashFunction(self, slots, storeelement):
        """
        This function is to store the given number in hashtable
        :param slots: total number of slots in hashtable
        :param storeelement: list of element to store on hashtable
        :return: it returns hastlist
        """

        hashlist = [None]*slots

        value = slots + 1
        for i in range(len(storeelement)):
                position = storeelement[i] % value

                if hashlist[position] == None and position < len(hashlist):
                    hashlist.pop(position)
                    hashlist.insert(position,storeelement[i])

                else:
                    k = 0
                    while k < len(hashlist):
                        k = k + 1
                        if (position+k) < len(hashlist) or position-k > 0:
                            if hashlist[position+k]==None:
                                hashlist.pop(position+k)
                                hashlist.insert(position, storeelement[i])
                                break
                            elif hashlist[position-k]==None:
                                hashlist.pop(position - k)
                                hashlist.insert(position, storeelement[i])
                                break


        return hashlist



    def hashSearch(self, key, hashlist, slots):
        """
         This function is to search the element on hash table
        :param key: data you wants to search
        :param hashlist: the hashtable on which elements are stored
        :param no_of_slots: number of slots in hash table
        """
        value = slots + 1

        for i in range(len(hashlist)):
                position = key % value #find the index from given data

                if hashlist[position]==key and position<len(hashlist):
                    print("key is present at",position,"index")
                    exit()

                else:
                    k = 0
                    while k < len(hashlist):
                        k = k + 1
                        if (position+k) < len(hashlist) or position-k >0:#check data on next index
                            if hashlist[position+k] == key:
                                print("key is present at", position+k, "index")
                                exit()
                            elif hashlist[position-k] == key: # check data on previous index
                                print("key is present at", position-k, "index")
                                exit()

hash = HashFunction()
