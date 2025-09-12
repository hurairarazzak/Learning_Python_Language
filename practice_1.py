# Let's Practice
# Write a Program to input 2 numbers & print their sum.

firstNum = int(input("Enter First Number:"))
secondNum = int(input("Enter Second Number:"))
print("The Both Number Sum is: ", firstNum + secondNum)

# Let's Practice
# WAP to input side of a square & print its area.

side = float(input("Enter the side of square: "))
print("The area of square is: ", side ** 2)

# Let's Practice
# WAP to input 2 floating point numbers & print their average.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average is: ", (a+b)/2)

# Let's Practice
# WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
print("Output is:", (a >= b))

# 📝 Lecture 1 – Side Practice Exercises (for you from chatGpt)
# 🔹Variables + Data Types
# 1) Aik variable city banao jisme apna city ka naam store ho aur uska type print karo.
# 2) x = 7, y = 3.5 do variables banao aur unka sum print karo. Type check bhi karo.
# 3) Aik variable me True store karo aur check karo uska type kya hai.

# 1) Question ka code
city = "Karachi"
print(type(city)) # Output Expected: <class 'str'>

# 2) Question ka code
x = 7
y = 3.5
print(x + y, type(x + y)) # Output Expected: 10.5 <class 'float'>

# 3) Question ka code 
booleanVal = True
print(type(booleanVal)) # Output Expected: <class 'bool'>

# 🔹 Operators
# 1) User se do numbers lo aur unka sum, difference, product, division print karo.
# 3) Ek program likho jo a = 10, b = 20 ke liye relational operators (>, <, ==) ka result print kare.

# 1) Question ka code
userNum1 = int(input("Enter the first number: "))
userNum2 = int(input("Enter the second number: "))
print("The sum is:", userNum1+userNum2)
print("The product is", userNum1*userNum2)
print("The division is", userNum1/userNum2)

# 2) Question ka code
a = 10
b = 20
print(("A is greater than b",a>b), ("A is less than b",a<b), ("A is equal to b",a==b), ("A is not equal to b",a!=b), ("A is greater than equal to b",a>=b), ("A is less than equal to b",a<=b) )

# 🔹 Assignment Operators
# 1) num = 2 rakho. Usme assignment operator se cube (num^3) calculate karo aur print karo.

# 1) Question ka code 
numCube = 3
numCube **= 3 
print(numCube)

# 🔹 Type Conversion
# 1) Ek program likho jo user se string input le "100" aur usse integer me convert karke 20 add kare.
# 2) Ek float number input lo (e.g. 52.6) aur usse int me convert karo.

# 1) Question ka code 
oneInp = str(input("Enter string number: "))
oneInp = int(oneInp) 
print(oneInp + 20, type(oneInp))

# 2) Question ka code
floatNum = float(input("Enter float number: "))
floatNum = int(floatNum)
print(floatNum, type(floatNum))

# 🔹 Input + Printing
# User se naam aur marks input lo aur print karo:
# "Hello Ali, you scored 85 marks" (string concatenation ka use karke).
# User se do numbers input lo aur unka average print karo.

# 1) Question ka code
userName = str(input("Enter your name: "))
userMarks = float(input("Enter your marks: "))
print("Hello "+userName+", you scored",userMarks)

# 2) Question ka code
pehlaNum = int(input("Enter first num: "))
dusraNum = int(input("Enter second num: "))
print( (pehlaNum + dusraNum)/2 )
