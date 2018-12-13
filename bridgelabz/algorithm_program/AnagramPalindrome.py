from com.bridgelabz.utility.Utility import Utility

# utility_obj = Utility()
# primenum = []
# primenum=utility_obj.getPrime()
# utility_obj.getPrimePalindrome(primenum)
# utility_obj.getPrimeAnagram(primenum)


utility_obj=Utility()
print("Enter the lower limit:")
lower_limit=utility_obj.inputIntiger()
print("Enter the upper limit:")
upper_limit=utility_obj.inputIntiger()
primenumber=[]
primenumber=utility_obj.getPrime(lower_limit,upper_limit)
utility_obj.checkPalindrome(primenumber)
utility_obj.checkAnagram(primenumber)