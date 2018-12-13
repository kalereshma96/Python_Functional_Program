def get_Int(self):
    return int(input())

#########################################################################
import random
import time
import math
class Utility:
    def __init__(self):
        pass

    def inputString(self):
        string=input("")
        return string

    def inputInteger(self):
        return int(input(""))

    def inputString(self):
        str1 = input(" ")
        return str1
    def string_replace(self, template, username):
        # Ensure UserName has min 3 char

        if len(username) < 3:
            print("Ensure that username has minimum 3 char..")
        else:
            result =str(template.replace("<<username>>", username))
            return result

    ##########################flip coin##################################
    def inputInt(self, flip):
        headcount = 0
        tailcount = 0
        per1 = 0
        per2 = 0

        for i in range(flip):
            if (flip < 0):
                print("Enter positive number:")

# Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
            else :
                val = random.random()
                print(val)
                if (val < 0.5):
                  tailcount = tailcount + 1
                else:
                  headcount = headcount + 1

    #Percentage of Head and Tails

        per1 = (tailcount * 100) / flip
        per2 = (headcount * 100) / flip
        print(tailcount)
        print(headcount)

        print("Percentage of tails ", per1)
        print("Percentage of heads ", per2)

    ########################################Leap Year###################################

    def inputYear(self, year):
# ensureentered year is a 4 digit number
         if len(str(year)) < 4:
             print("Enter 4 digit number...")
         else:
            #print(year)

             if (year % 4 == 0 and year % 400 == 0 and year % 100 == 0):
                 print(year ," is leap year")
             else:
                print(year, "not a leap year")

    ######################################## power of two ############################
    #This program takes a command-line argument N and prints a table of the powers
    # of 2 that are less than or equal to 2^N.

    def inputPower(self,power):
         temp =1
         for i in range(1, power+1):
             temp = temp * 2

         if power > 31:
             print("enter value less than 31")
         else:
             print(power, "of is", temp)

    ################################# Harmonic Number ##############################
        #This function gives the Nth Harmonic Value.


    def inputNumber(self,number):
            result = 0
            for i in range(1, number+1):
               if number!=0: #Ensure that number is not equal to zero
                     result = result + (1/i)

               else:
                     print("enter greater than 0 value..")
            print("the harmonic value of ", number, 'is', result)

      ############################## Prime factors ###################################

           #This function  Print the prime factors of number N.


    def  inputPrimeno(self,num):

        for i in range(2, num):
                while num % i == 0:
                  num = num / i

                  print(i, " ")

               # if num > 2:
                # print(num)


     ##################################### Gambler ####################################

         # Play till the gambler is broke or has won
         #Print Number of Wins and Percentage of Win and Loss.

    def getInput(self,stake,goal,NoofTimes):


        wins = 0

        for i in range(0, NoofTimes):
            money = stake

            while (money > 0 and money < goal):
                #bets = bets +1

                val = random.randint(0,1)
                if val < 0.5:
                    money = money + 1
                else:
                    money = money - 1

                if money == goal:
                    wins = wins + 1

        perofWins = (100 * wins) / NoofTimes
        perofLoss = 100 - perofWins

        return wins, perofWins, perofLoss
    ############################ Coupon Number ###################################


  #  def getCouponNo(self, num):




  ################################ Two D-Array ####################################
  # M rows, N Cols, and M * N inputs for 2D Array.

    def getArray(self, n, m):
        arr = []
        for i in range(n):
            print("enter values:")
            element = []

            for j in range(m):
             val = input(" ")
             element.append(val)

             arr.append(element)
   #File handiling.create array.txt file.program output i.e arr will
   #get wrote into that file.
            file = open("array.txt", "w")
            file.write(str(arr))
            file.close()
           # arr[i][j] = Utility().get_Int()
        print(arr)


  ############################### Sum of int ###########################################
    #Read in N integers and counts the   number of triples that sum to exactly 0.

    def getEle(self,number):
        store_ele = []
        print("Enter values..")
        for i in range(number):
            x = int(input(" "))
            store_ele.append(x)
        return store_ele
    def getSum(self,number, s):

        count = 0
        flag = 0
        print("Triplet is..")
        for i in range(0, number-2):
            for j in range(i+1, number-1):
                for k in range(j+1, number):
                   if(s[i] + s[j] + s[k] == 0):
                       print(s[i], s[j], s[k])
                       count = count + 1
                       flag = 1
        print("total triplet count is:", count)


        if flag == 0:

           print("triplet is not found...")
 ############################# Stop Watch ############################################


    def getStart(self):
      starttime = time.time()
      return starttime
    def getStop(self):
       stoptime = time.time()
       return stoptime






    ######################## Permutation ###########################
    
    # def permutations(self, string):
    #     # stores all generated permutations
    #
    #     if len(string) <= 1:
    #         return string
    #
    #         # for e in range(int(string[: len(string-1)])):
    #         #     for i in range (len(e) + 1):
    #         #       perms.append(e[:i] + string[-1] + e[i:])
    #
    #     perms = []
    #     for i in string:
    #        permute = permutations(string.replace(i, ""))
    #        for j in permute:
    #          perms.append(j + i)
    #
    #
    #          print(perms)
    #
    #
    #


    # def permutations(self, s):
    #     start = []
    #     if(len(s) == 0):
    #          start = [s]
    #
    #     else:
    #         for i,c in enumerate(s):
    #           for j in range(s[:i] + s[i+1:]):
    #             #  start = start + c
    #      return start
            
    ############################# Quadatic ###########################
    def getQuadratic(self, a, b, c):
        delta = (b * b )- (4 * a * c)
        root1 = int(-b + math.sqrt(delta))/(2*a)
        root2 = int(-b - math.sqrt(delta))/(2*a)

        if(root1 == 0 and root2 == 0):
            print("enter a and c value smaller than b")
        else:


           print("root 1 is:",root1)
           print("root 2 is:",root2)

    ################################# wind chill #########################3
    #Its take two command line argument t as temperature and v as speed.
    def getWindchill(self, t, v):
        if (t > 50 or (v > 120 or v < 3)):
            print("Enter valid temperature and speed...")
        else:

            w = (35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16))

        print("temperature is:", t)
        print("speed is:", v)
        print("wind chill:", w)



    # ############################## Prime Number #########################
    #
    # def getPrime(self):
    #     flag = 0
    #     storeprime = []
    #     for i in range(3, 1000):
    #
    #         for j in range(2, i):
    #             if i % j == 0:
    #                 flag = False
    #                 break
    #             else:
    #                 flag = True
    #         if flag == True:
    #            storeprime.append(i)
    #     return storeprime
    # #################### Anagram Detection ###################################
    #
    # def getAnagram(self, str1, str2):
    #     # print(str1,str2)
    #     # #flag = 0
    #     a = []
    #     b = []
    #     str1 = str1.replace(" "," ")
    #     str2 = str2.replace(" "," ")
    #     if(len(str1) == len(str2)):
    #         # flag=1
    #         print(str1," and",str2,"anagram of each other..")
    #     else:
    #         #flag =0
    #         print("enter strings are not anagram ")
    #
    #     #if flag == 1:
    #     a.append(str1)
    #     b.append(str2)
    #     return a,b
    #
    # ################### Prime Anagram Palindrome #######################
    #
    # # def getPrimePalindrome(self,primenum):
    # #     print("Prime palindrome numbers are..")
    # #
    # #     for i in range(len(primenum)):
    # #        sum = 0
    # #        if(primenum[i] > 0):
    # #          no = primenum[i]
    # #
    # #          while (no > 0):
    # #            r = no % 10
    # #            no = no // 10
    # #            sum = sum * 10 + r
    # #
    # #          no=primenum[i]
    # #        if (no == sum):
    # #            print(sum)
    # # def getPrimeAnagram(self,primenum):
    # #     print(primenum)
    # #     print("Prime anagram numbers are..")
    # #     for i in range(len(primenum)):
    # #         for j in range(len(primenum)):
    # #             if (primenum[i] > 0 and primenum[j] > 0):
    # #                 str1 =str(primenum[i])
    # #                 str2 =str(primenum[j])
    # #                 Utility().getAnagram(str1,str2)
    # #                 #print(str1,str2)
    #
    # def checkPalindrome(self, primenumber):
    #     for i in range(len(primenumber)):
    #         reversenum = 0
    #         if primenumber[i] > 0:
    #             temp = primenumber[i]
    #             while temp > 0:
    #                 r = temp % 10
    #                 temp = temp // 10
    #                 reversenum = reversenum * 10 + r
    #             temp = primenumber[i]
    #             if temp == reversenum:
    #                 print(reversenum, " is a palindrome")
    #
    # def checkAnagram(self, primenumber):
    #     print("The prime number which are Anagram:")
    #     for i in range(len(primenumber)):
    #         for j in range(len(primenumber)):
    #             if primenumber[i] > 0 and primenumber[j] > 0:
    #                 string1 = str(primenumber[i])
    #                 string2 = str(primenumber[j])
    #                 self.getAnagram(string1, string2)
    def anagramLogic(self, string1, string2):
        string1 = string1.replace(" ", "")
        string2 = string2.replace(" ", "")

        lowercasestring1 = string1.lower()
        lowercasestring2 = string2.lower()

        str1_removeduplicates = "".join(set(lowercasestring1))
        str2_removeduplicates = "".join(set(lowercasestring2))

        count = 0
        if len(str1_removeduplicates) == len(str2_removeduplicates):
            for i in range(len(str1_removeduplicates)):
                for j in range(len(str1_removeduplicates)):
                    if str1_removeduplicates[i] == str2_removeduplicates[j]:
                        count = count + 1

        if count == len(str1_removeduplicates) or string1 == string2:
            print(string1, "and", string2, " are an Anagram")
        else:
            print(string1, "and", string2, " are an not Anagram")

        ######################################################################################

    def getPrime(self, lower_limit, upper_limit):
        storeprime = []

        i = lower_limit

        for i in range(upper_limit):
            isprime = False
            if i == 0 and i == 1:
                continue
            for j in range(2, i):
                if i % j == 0:
                    isprime = False
                    break
                else:
                    isprime = True

            if isprime == True:
                storeprime.append(i)

        return storeprime
        ###########################################################################################

    def checkPalindrome(self, primenumber):
        for i in range(len(primenumber)):
            reversenum = 0
            if primenumber[i] > 0:
                temp = primenumber[i]
                while temp > 0:
                    r = temp % 10
                    temp = temp // 10
                    reversenum = reversenum * 10 + r
                temp = primenumber[i]
                if temp == reversenum:
                    print(reversenum, " is a palindrome")

    def checkAnagram(self, primenumber):
        print("The prime number which are Anagram:")
        for i in range(len(primenumber)):
            for j in range(len(primenumber)):
                if primenumber[i] > 0 and primenumber[j] > 0:
                    string1 = str(primenumber[i])
                    string2 = str(primenumber[j])
                    self.anagramLogic(string1, string2)

    ############################ Static methods ###############################
    # def getBinaryInt(self):
    #     s =int(input("Enter size of array:"))
    #     array_size = [s]
    #     x = len(array_size)
    #     print("Enter array element:")
    #     for i in range(0, s):
    #         num =int(input(" "))
    #         array_size.append(num)
    #     number=int(input("Enter number to be search.."))
    #     lower = 0
    #     upper = s
    #     mid = upper + lower // 2
    #
    #     for i in range(0, len(array_size)):
    #         if number > array_size[mid]:
    #             lower = mid +1
    #         else:
    #             number == array_size[mid]
    #
    #             print("number found at ",mid,"index position")
    #             break
    #
    #         if number < array_size[mid]:
    #             upper = mid -1
    #
    #
    #         while x > 0:
    #             mid = upper + lower // 2
    #             x = x -1
    #             break
    #
    #         for j in range(len(array_size)):
    #           if(number != array_size[j]):
    #             print("Number not found..!!!")
    #
    #
    #
    #
    # def getBinaryStr(self):
    #     s =int(input("Enter size of array:"))
    #     array_size = [s]
    #     str_array= [s]
    #     print("Enter array element..")
    #     for i in range(0, s):
    #         array_size[i] =int(input(" "))
    #         for j in range(0, s):
    #            str_array[j]=int(input(" "))
    #            str1 =int(input(" "))
    #            array_size.append(str1)
    #     print("array_size.append(num)   Enter string to be searched..")
    #
    #     lower = 0
    #     upper = len(str_array)- 1
    #     mid = upper + lower // 2
    #     x = len(str_array)
    #     for i in range(0,len(str_array)):
    #         if (str1 < 0) :
    #             lower = mid +1
    #         if(str1 == str_array[mid]):
    #             print("string found at ",mid,"index position")
    #         if(str1 > 0):
    #             upper = mid +1
    #
    #         while x > 0:
    #               mid = upper + lower // 2
    #               x = x -1
    #               break
    #         for j in range(0, str_array):
    #             if(str1 != str_array[j]):
    #                  print("string not found")
    #
    #
    # def choice(self):
    #
    #
    #     print("1.Binary search method for integer")
    #     print("2.Binary search method for string")
    #     # print("3.Insertion sort method for integer")
    #     # print("4.Insertion sort method for string")
    #     # print("5.Bubble sort method for integer")
    #     # print("6.Bubble sort method for string")
    #     #
    #
    #     choice =int(input(" "))
    #
    #
    #
    #
    #     if choice == 1:
    #        Utility().getBinaryInt()
    #     if choice == 2:
    #         Utility().getBinaryStr()
    #     # if choice == 3:
    #     #    choice.getInsertionInt()
    #     # if choice == 4:
    #     #    choice.getInsertionStr()
    #     # if choice == 5:
    #     #    choice.getBubbleInt()
    #     # if choice == 6:
    #     #     choice.getBubbleStr()
    #
    # # def getInsertionInt(self):
    # def getStringElement(self, s):
    #     newlist = []
    #     for i in range(s):
    #         num = int(input(""))
    #         newlist.append(num)
    #     return newlist
    #
    # def getInsertion(self, storeelement):
    #
    #     print(storeelement)
    #
    #     for i in range(1, len(storeelement)):
    #         temp = storeelement[i]
    #         j = i - 1
    #
    #         while (temp <= storeelement[j] and j >= 0):
    #             storeelement[j + 1] = storeelement[j]
    #             j = j - 1
    #
    #         storeelement[j + 1] = temp
    #     print("in ascending order")
    #     for i in range(0, len(storeelement)):
    #         print(storeelement[i])
    # # #
    # # def getInsertioStr(self):
    # #
    # #
    # # def getBubbleInt(self):
    # # def getIntElement(self,s):
    #         newlist = []
    #         for i in range(s):
    #             num = int(input(""))
    #             newlist.append(num)
    #         return newlist
    #
    #
    #
    #     def getBubble(self,storeelement):
    #
    #         print(storeelement)
    #         n =len(storeelement)
    #         for i in range(len(storeelement)):
    #             for j in range(0, n-i-1):
    #                 if storeelement[j] > storeelement[j+1]:
    #                   storeelement[j],storeelement[j+1]=storeelement[j+1],storeelement[j]
    #         print("sorted array is")
    #         for i in range(len(storeelement)):
    #             print(storeelement[i])
    # # def getBubbleStr(self):

########################### Find Number ######################3333

    def getNum(self,no):
        lower = 0
        upper = no - 1
        mid = upper + lower // 2
        count = 0

        print("the range of no", lower, "-", upper)
        print("the imagined no is:", mid)
        number = int(input("enter 1 for high,2 for low,0 or yes"))
        while lower <= upper:
            if number == "1":
                lower = mid
                count = count + 1
            elif number == "2":
                upper = mid
                count = count + 1
            elif number == "0":
                count = count + 1
                print("the imagined no is", mid)
                break

            if count < no:
                mid = upper + lower // 2
                print("your imagined no at", mid)

    ###################### Word From List ########################

    def getWord(self,storeelement):

      word=input("enter word to be search..")
      for i in range(0, len(storeelement)):
          print(storeelement[i])
      file = open("word.txt", "w")
      file.write(str(storeelement))
      file.close()
      file = open("word.txt", "r")
      if file.mode == 'r':
          contents = file.read()
          print(contents)
      lower = 0
      upper = len(storeelement)- 1
      mid = upper + lower // 2
      x = len(storeelement)
      lineno = word
      for i in range(0, len(storeelement)):

            if word > storeelement[mid]:
                lower = mid +1
            else:
                word == storeelement[mid]

                print("number found at ",mid,"index position")
                break

            if word < storeelement[mid]:
                upper = mid -1


            while x > 0:
                mid = upper + lower // 2
                x = x -1
                break

            for j in range(len(storeelement)):
              if(word != storeelement[j]):
                print("word not found..!!!")



    ###################### Insertion sort ################################
    def getStringElement(self,s):
        newlist=[]
        for i in range(s):
            num=input("")
            newlist.append(num)
        return newlist

    def getInsertion(self,storeelement):


        print(storeelement)

        for i in range(1,len(storeelement)):
             temp = storeelement[i]
             j =  i - 1

             while (temp <= storeelement[j] and j >= 0):
                 storeelement[j+1] = storeelement[j]
                 j=j-1

             storeelement[j + 1] = temp
        print("in ascending order")
        for i in range(0,len(storeelement)):
            print(storeelement[i])
        file = open("insertion.txt", "w")
        file.write(str(storeelement))
        file.close()
        file = open("insertion.txt","r")
        if file.mode == 'r':
            contents = file.read()
            print(contents)
           # print(contents[0])
            #print(word)
 ########################## Bubble Sort #####################
    def getIntElement(self,s):
        newlist = []
        for i in range(s):
            num = int(input(""))
            newlist.append(num)
        return newlist



    def getBubble(self,storeelement):

        print(storeelement)
        n =len(storeelement)
        for i in range(len(storeelement)):
            for j in range(0, n-i-1):
                if storeelement[j] > storeelement[j+1]:
                  storeelement[j],storeelement[j+1]=storeelement[j+1],storeelement[j]
        print("sorted array is")
        for i in range(len(storeelement)):
            print(storeelement[i])
        file = open("bubble.txt", "w")
        file.write(str(storeelement))
        file.close()
        file = open("bubble.txt", "r")
        if file.mode == 'r':
                contents = file.read()
                print(contents)

######################## MERGE SORT ##############################


    # for i in range(0, n):
    #   for j in range(0, n):
    #        for k in range(0, n):
    def getMerge(self, storelement):
        print(storelement)
        mid = len(storelement)//2
        #print(mid)

        n = len(storelement)
        lefthalf = storelement[:mid]
        righthalf = storelement[mid:]
        i = 0
        j = 0
        k = 0
      #  Utility().getMerge(lefthalf)
       # Utility().getMerge(righthalf)

        while i < len(lefthalf) and j >len(righthalf):
            if lefthalf[i] < righthalf[i]:
                 storelement[k]=lefthalf[i]
                 i = i+1
            else:
                 storelement[k]=righthalf[j]
                 j = j+1
            k = k+1
        while i < len(lefthalf):
            storelement[k]=lefthalf[i]
            i = i+1
            k = k+1
        while  j <len(righthalf):
            storelement[k]=righthalf[j]
            j=j+1
            k=k+1
        Utility().getMerge(storelement)
        print("merging:",storelement)

   ##################### Day of week #######################

    def getDay(self,m,d,y):


        y0 = y - (14 - m) / 12

        x = y0 + y0 / 4 - y0 / 100 + y0 / 400

        m0 = m + 12 * ((14 - m) / 12) - 2

        d0 = (d + x + 31 * m0 / 12) % 7

        return d0
 ########################## Temperature ################################
    def getTemp(self,temp):

         choice = 0

         print("Enter 1 for fahrenheit and 2 for celsius")
         choice =int(input(" "))

         if choice == 1:
           F = (temp * 9 / 5) + 32
           print("In fahrenheit",F)

         elif choice == 2:
           F = (temp - 32) * 5 / 9
           print("In celsius",F)
        # res = input(temp)

       # Celsiustoahrenheit=(°C × 9/5) + 32 = °F
       # FahrenheittoCelsius=(°F − 32) x 5/9 = °C

    ######################### Monthly payment ####################

    def getPrinciple(self,principle, year, rate):
        n = 12 * year
        R1 = rate / (12 * 100)
        payment = (principle * R1) / (1 - (pow((1 + R1), -n)))
        print(payment)
    ######################### Square root ########################

    def getSqrroot(self,result):
        c = result
        t = c
        epsilon = 1e-15
        while (math.fabs(t - c / t) > epsilon * t):
            t = (c / t + t) / 2.0
        print(t)
    ############################ Decimal to binary #############
    def getBinary(self, no):
        print("binary of:",no,"is")
        rem = 0
        binary = 0
        i = 1
        while no != 0:
            rem = no % 2
            no = no // 2
            binary = binary + rem * i
            i = i * 10  # until i becomes zero
        print(binary)
    ####################### binary to binary #####################
    def getToBinary(self,no):

        rem = 0
        binary = 0
        i = 1
        print("binary of :", no)
        while no != 0:
            rem = no % 2
            no = no // 2
            binary = binary + rem * i
            i = i * 10  # until i becomes zero
       # print(binary)

        binary=str(binary)
        binary=binary.zfill(8)
        print(binary)
        store =binary
        #print(store)
        n =len(str(store))
        mid = n//2
        mid = len(store) // 2
        n = mid
        nibbbleone =store[:mid]
        nibbletwo = store[mid:]
        print("first nibble:",nibbbleone)
        print("second nibble:",nibbletwo)
        print("after swapping...")
        temp = nibbbleone
        nibbbleone=nibbletwo
        nibbletwo=temp
        print(nibbbleone)
        print(nibbletwo)
        storeelement =nibbbleone+nibbletwo
        print(storeelement)
        print("decimal of:",storeelement)
        num = int(storeelement)

        #int(input(storeelement))
        decimal = 0
        i = 1
        while num != 0:
              remd = num % 2
              decimal = decimal + remd * i
              num = num // 10
              i = i * 2
        print(decimal)
       # power = 0
        #for i in range(len(storeelement)):

    #######################Data #####################################





















































  