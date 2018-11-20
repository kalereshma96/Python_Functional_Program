def get_Int(self):
    return int(input())

#########################################################################
import random
import time
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

    def getSum(self,number):

        s = []
        count = 0

        for i in range(0, number-2):
            for j in range(i+1, number-1):
                for k in range(j+1, number):
                   if(s[i] + s[j] + s[k] == 0):
                       print(s[i]+s[j]+s[k])
                       count = count + 1

                       if count == 0:
                           print("triplet is not found...")
 ############################# Stop Watch ############################################


    # def getStart(self,startTime):
    #     startTime=0
    #       startTime = time.time()
    # def getStop(self, stopTime):
    #     stopTime=0
    #       stopTime = time.time()
    #
    #  print("elapsed time is:", stopTime - startTime)
    #
    #
    #


