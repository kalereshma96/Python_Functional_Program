#Take User Name as Input and Replace String Template "Hello <<username>>  How are you?"

from com.bridgelabz.utility.Utility import Utility
template = 'Hello <<username>>  How are you?'
utility_obj = Utility()
print("Enter the name:")
username = utility_obj.inputString()  # type: object
result = utility_obj.string_replace(template, username)
print(result)