# Basic Operation String concatenation & length (len) of str
str1 = "This is a string.\nWe are creating it in python"
print(str1)

concatStr1 = "Huraira"
len1 = len(concatStr1)
print(len1)

concatStr2 = "Razzak"
len2 = len(concatStr2)
print(len2)

finalStr = concatStr1 + " " + concatStr2
len3 = len(finalStr)
print(finalStr)
print(len3)

# Indexing in Python
indexingStr = "Huraira"
print(indexingStr[0])

# Error bcz in python we can only
# access character but we can't manipulate character 
# we can't modify them
# str = "Razzak"
# str[5] = "q"
# print(str)

# Slicing in Python
sliStr = "HurairaRazzak"
print(sliStr[1:4])
print(sliStr[:4]) # [0:4]
print(sliStr[5:]) # [5:len(sliStr)] iska mtlb bhi same
print(sliStr[5:len(sliStr)]) # len(sliStr) iska mtlb 5 length ke baad string ke end tak

# Slicing Negative Indexing
fruitStr = "Apple"
print(fruitStr[-3:-1])

# String Functions
funcStr = "i'm studying python from youtube."
print(funcStr.endswith("youtube")) #returns true if string ends with substring

# print(str.capitalize(funcStr)) #capitalizes 1st char and make new string
funcStr = str.capitalize(funcStr)
print(funcStr) 

print(funcStr.replace("python", "javascript")) # This will replace the python word to javascript word
 
print(funcStr.find("u")) # So this will find the index number of first 
# written character "u" in  the string

print(funcStr.count("y")) # this means letter y kitni baar exist karta hae 
# hamare string mae tou yae utne number btayega apko kae itni bar "y" hae
# string mae

# Conditional Statements
# if-elif-else (SYNTAX)

# age = 21
# if(age >= 18):
#     print("Can vote")
#     print("Can drive")

light = "red"

if(light == "red"):
    print("Stop your car")
elif(light == "green"):
    print("You can go now")
elif(light == "yellow"):
    print("Look")
else:
    print("Light is broken") # The 4 tab space is called indentation

print("end of code")

# Conditional Statements
# Grade students based on marks

# marks >= 90, grade = "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks, grade = "D"

marks = int(input("Enter you marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the Student:", grade)

# Nesting in Conditional Statements
age = int(input("Enter Your Age: "))
if(age >= 18):
    if(age >= 80):
        print("Too Old Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Too Young Cannot Drive")

