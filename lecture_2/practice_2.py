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
    print(f"The largest number is: {a}")
elif(b >= a and b >= c):
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")

# 3) Question ka code
x = int(input("enter the number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")


# Side Practice Ye wale karo (chhote aur useful, bina extra concept ke):
# 1) Password Check
# User se ek password input lo.
# Agar "admin123" hai to print karo "Access Granted".
# Warna "Access Denied".

# 2) Movie Ticket Pricing
# User se age input lo.
# Agar age < 13 → "Child Ticket = 500"
# Agar 13 ≤ age < 60 → "Adult Ticket = 1000"
# Agar age ≥ 60 → "Senior Ticket = 700"

# 3) String Analysis
# User se ek string input lo aur print karo:
# Uski length
# Pehla character
# Last character

# 4) Find Vowel Count
# Ek program likho jo user ke diye gaye string me 
# kitne vowels (a, e, i, o, u) hain wo count kare.

# 1) Side prac question ka code
userPass = input("Enter your password: ")
if(userPass == "admin123"):
    print("Access Granted")
else:
    print("Access Denied")

# 2) Side prac question ka code 
userAge = int(input("Enter your age: "))
if(userAge < 13):
    print("Child Ticket = 500")
elif(userAge >= 13 and userAge < 60):
        print("Adult Ticket = 1000")
else:
    print("Senior Ticket = 700")

# 3) Side prac question ka code
userStr = str(input("Enter the input: "))
if len(userStr) > 0:
    print("The String length is", len(userStr))
    print("First character is:", userStr[0])
    print("Last character is:", userStr[-1])
else:
    print("Empty string, no characters!")

# 4) Side prac question ka code
vowelCount = str(input("Enter the paragraph to find vowels: "))
print(vowelCount.count("a") + vowelCount.count("e") + vowelCount.count("i") + vowelCount.count("o") + vowelCount.count("u"))