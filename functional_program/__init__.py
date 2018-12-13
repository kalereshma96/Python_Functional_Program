#Take User Name as Input and Replace String Template "Hello <<username>>  How are you?"

#import string
class Stringreplace

str = 'Hello <<username>>  How are you?'
name = input("Enter a name:")
string_function()
#Ensure UserName has min 3 char
if len(name) < 3:
    print("enter more than 3 char")
else:
    print(name)

new_str = str.replace('<<username>>', name)
# Print the String with User Name

print(new_str)