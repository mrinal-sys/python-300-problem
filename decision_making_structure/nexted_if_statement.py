# nested if statement means, if statement inside another if statement block
# syntax
#  if(condition1):
#      if(condition2):
#          statement or set of statement
# When condition 1 is true then condition2 will be checked and inside 2nd if statement block, 
# all the statement or set of statement will be execute if both the condition become statisfied.

num = 18
if (num%2 == 0):
    if(num%3 ==0):
        print("Number is divisible by 3 and 2")
else:
    print("Both are not divisble by 2")


name = str(input("Enter your Name"))
age = int(input("Enter your age"))
if(name == "Mrinal"):
    if(age == 26):
        print("Valid User")
else:
    print("Invalid user")
     