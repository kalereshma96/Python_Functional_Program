#Take input N distinct Coupon Numbers from user. Print how many random numbers do you
#need to generate distinct coupon number.

from com.bridgelabz.utility.Utility import Utility

utility_obj = Utility()
num = int(input("Enter number"))
num = utility_obj.getCouponNo(num)

