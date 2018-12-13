from com.bridgelabz.utility.Utility import Utility
# utility_obj14 = Utility()
# primenum=[]
# primenum=utility_obj14.getPrime()
# print(primenum)


utility_obj=Utility()
print("Enter the lower limit:")
lower_limit=utility_obj.inputIntiger()
print("Enter the upper limit:")
upper_limit=utility_obj.inputIntiger()
primenumber=[]
primenumber=utility_obj.getPrime(lower_limit,upper_limit)
print("prime numbers are:")
print(primenumber)