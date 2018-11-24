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
    def getWindchill(self, t, v):
        if (t > 50 or (v > 120 or v < 3)):
            print("Enter valid temperature and speed...")
        else:

            w = (35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16))

        print("temperature is:", t)
        print("speed is:", v)
        print("wind chill:", w)



    ############################## Prime Number #########################

    def getPrime(self):
        flag = 0
        storeprime = []
        for i in range(3, 1000):
            
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True:
               storeprime.append(i)
        return storeprime
    #################### Anagram Detection ###################################

    def getAnagram(self, str1, str2):
        #flag = 0
        a = []
        b = []
        str1 = " "
        str2 = " "
        if(len(str1) == len(str2)):
            # flag=1
            print("enter strings are anagram of each other..")
        else:
            #flag =0
            print("enter strings are not anagram ")

        #if flag == 1:
        a.append(str1)
        b.append(str2)
        return a,b

    ################### Prime Anagram Palindrome #######################

    def getPrimePalindrome(self,primenum):
        print("Prime palindrome numbers are..")

        for i in range(len(primenum)):
           sum = 0
           if(primenum[i] > 0):
             no = primenum[i]

             while (no > 0):
               r = no % 10
               no = no // 10
               sum = sum * 10 + r

             no=primenum[i]
           if (no == sum):
               print(sum)
    def getPrimeAnagram(self,primenum):
        print("Prime anagram numbers are..")
        for i in range(primenum):
            for j in range(len(primenum)):
               str1 =str1(primenum[i])
               str2 =str2(primenum[j])
            if(primenum[i] == 0 and primenum[j] == 0):
                self.getAnagram(str1,str2)

            print(str1,str2)

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
    # #
    # #
    # # def getInsertioStr(self):
    # #
    # #
    # # def getBubbleInt(self):
    # #
    # # def getBubbleStr(self):

########################### Find Number ######################3333


    def getMagicNo(val, lower, upper, mid):
        num_array =[]
        print("Your number is :",mid)
        print("Enter yes or high or low")

        no = int(input(" "))
        num_array.append(no)

        count = 0

        for i in range(0, val):


            if( no):
                low = mid + 1
                count = count +1


            elif no == num_array[mid]:
                 print("Number found at",mid,"index position")

            else:
                 no > num_array[mid]
                 upper = mid - 1
                 print("2".mid,"-",upper)

            print("Intermediary numbers are",low,"and",high)


    ###################### Word From List ########################

    def getWord(self,word_list):
      #word = []
      flag = 0
      word=input("enter word to be search..")
      word.append(word_list)

      for word in range(word_list):


         if flag == 0:
            print("Word not found")
         if flag == 1:
           print("word found")
      file = open("word_list.txt", "w")
      file.write(str(word_list))
      file.read(word)
      file.close()
      print(word)

    ###################### Insertion sort ################################

    def getInsertion(self,s):

    System.out.println("enter elements in strings");
    for (int k = 0; k < s; k++) {
        arr[k] = scanner.next();
    }
    int
    n;
    String
    temp;
    for (int i = 1; i < s; i++) {
        temp = arr[i];
    int j = i - 1;
    while (j >= 0) {
    if (temp.compareTo(arr[j]) > 0) {
    break;
    }
    arr[j + 1] = arr[j];
    j - -;
    }
    arr[j + 1] = temp;
    System.out.println(Arrays.toString(arr));
    }
    return arr;

}

















































  