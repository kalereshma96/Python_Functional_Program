from collections import deque
###################################Data Stucture###################
class Data_structure:
    def palindrome(self):
        print("ghj")
############################Balance parathenses ####################


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

    # def searchFromFile(self):
    #     """
    #     This function read the data from file and store it on linked list.
    #     user will enter the element to search if it is present in linked list
    #     then that element is poped from list else element is added on list
    #     """
    #     fileobject = open("inputword.txt", "w+")  # create file object for read write operation
    #     list = ["rohini ", "reshma", "rajat ", "sai ", "akansha"]
    #     fileobject.writelines(list)  # write data on file
    #     fileobject.close()  # close file
    #
    #     fileojbect = open("inputword.txt", "r")  # open file for reading data
    #
    #     storefilecontent = fileojbect.read()
    #     storefilecontent = str(storefilecontent).split()
    #     # print(storefilecontent)
    #     fileojbect.close()
    #
    #     for i in range(len(list)):
    #         ol.append(list[i])
    #
    #     ol.display()
    #
    #     key = input("Enter the Element you want to search:")
    #     result = ol.searchElement(key)
    #     print(result)
    #
    #     if result == False:
    #         ol.append(key)
    #     else:
    #         ol.pop(key)
    #
    #     ol.display()
ol = OrderedList()

########################## Stack #################################
class Stack():
    top = -1
    stackSize =15
    def __init__(self):
        self.stack =list ()
    def push(self,data):
        if len(self.stack) > self.stackSize:#initially stack is full
            print("Stack is full..overflow condition..")
        else:
            top = +1
            self.stack.insert(top, data) #insert data on top

            #self.stack[top]= x
    def isEmpty(self):
        if self.top == -1:
            return  True
        else:
            return  False

    def pop(self):
        if self.top == -1:
            print("stack is empty....underflow condition")
        else:
            top = self.top
            temp = self.stack[top]
            self.stack.pop()
            top -= 1
            return temp
           # top = self.top-1
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


        if st.size()== -1:
            print("Expression is balanced..!!!")
        else:
            print("expression is not balanced..!!")

    def anagram_stack(self):
        """
        This method is used to print prime anagram in reverse order.
        :return: nothing
        """
        for i in utility_obj.get_anagram_prime():
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
        rear=0
        if(self.rear < self.size):
            self.queue[self.rear]=data
            rear = rear + 1
            return self.rear
        else:
            print("queu is full")


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

   # count = 0
    #flag = True
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
    def deposit(self):
        amount = int(input("Enter amount to be deposite."))
        balance=+ amount
        q.enqueue(balance)
        print("Balance is",balance)

    def withdraw(self,balance):
        withdrawal = int(input("Enter amount to be withdraw."))
        if(withdrawal < balance):
            q.deque()
            bal = balance - withdrawal
            balance = balance - withdrawal
            print("Balance is ", balance)
        else:
            print("Insufficient balance..")

    def current_balance(self,balance):
        print("Current balance is",balance)

    def persons_in_queue(self,):
       number = q.sizeOfQue()
       print("Number of persons in queue",number)

    def choice(self):
        flag = True
        choice = int(input(" "))
        if choice == 1:
          self.deposite()
        if choice == 2:
          self.withdraw()
        if choice == 3:
          self.current_balance()
        if choice == 4:
          self.persons_in_queue()
          while (flag == True):
              count =count+1
        print("Do you want to continue transaction...")
        print("Press True or false..")

    def anagramQueue(self):
        """
        This method is used to print prime anagram using queue.
        :return:
        """

        for i in utility_obj.get_anagram_prime():
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
#utility_obj = Utility()
def primeTwoDarray(self):
    """
    This method is used to store prime number in matrix or 2d array
    and print in proper order.
    :return: nothing
    """

    prime_list = utility_obj.get_prime()
    row = 10
    column = 25
    limit = 100

    twoDarray = [[0 for j in range(column)] for i in range(row)]

    k = 0
    for i in range(row):

        for j in range(column):

            if k < len(prime_list):
                if prime_list[k] <= limit:
                    twoDarray[i][j] = prime_list[k]
                    k += 1

        limit += 100

    for i in range(row):

        for j in range(column):

            if twoDarray[i][j] != 0:
                print(twoDarray[i][j], end=" ")

        print()
 ###########################################################################3
