"""
purpose   : To implement the all the operations of stack,and check
            given expression is having balance parentheses
@Author   : Reshma Y. Kale
@version  : 1.0

"""


#support mathematical operations like union,
# intersection, difference, and symmetric difference.
#Curly braces or the set() function can be used to create sets.
# #  Note: to create an empty set you have to use set(), not {}
# basket = {'apple','grapes','apple','orange'}
# #its remove duplicate values
# 'orange' in basket #fast membership testing,if item is present in the list its return true
# print(basket)

#set operations
a = set('asdfasdfthjk')
b = set('asdgvbnjyt')
print(a)
print(b)

a - b #lettrs in a but not in b
print(a-b)
a|b # letters in a or b or both
print(a|b)
a&b #letters in both a and b
print(a&b)
a ^ b # letter in a or b or not in both
print(a^b)