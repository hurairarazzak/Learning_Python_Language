# Let‘s Practice
# WAP to input user’s first name & print its length.
# WAP to find the occurrence of ‘$’ in a String.

# 1) Question ka code
userName = str(input("Enter Your First Name: "))
print("Your Name length is:", len(userName))

# 2) Question ka code
occurrenceStr = "Hey $, it's a pleasure to meeting with you $, Thanks $"
print("There are",occurrenceStr.count("$"), "$ sign in string")

# Let‘s Practice
# WAP to check if a number entered by the user is odd or even.
# WAP to find the greatest of 3 numbers entered by the user.
# WAP to check if a number is a multiple of 7 or not.

# 1) Question ka code 
chkNum = int(input("Enter the number to check odd or even: "))
if(chkNum % 2 == 0):
    print("Your number is even")
else:
    print("Your number is odd")

# 2) Question ka code
a = int(input("Enter your a number: "))
b = int(input("Enter your b number: "))
c = int(input("Enter your c number: "))

if(a >= b and a >= c):
    print("A is the big number in all")
elif(b >= a and b >= c):
    print("B is the big number in all")
else:
    print("C is the big number in all")

# 3) Question ka code
x = int(input("enter the number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")