# Let's Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1, "abc", "abc", 1]
# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]
# Store the above values in a list & sort them from "A" to "D"

# 1) Question ka code
favMovieList = []
favMovie1 = str(input("Enter your first favorite movie name: "))
favMovie2 = str(input("Enter your second favorite movie name: "))
favMovie3 = str(input("Enter your third favorite movie name: "))

favMovieList.append(favMovie1)
favMovieList.append(favMovie2)
favMovieList.append(favMovie3)

print(favMovieList)

# OR ALTERNATE WAY THIS WAY THE CODE LINES IS LESS Both are correct

favMovieList.append(str(input("Enter your first favorite movie name: ")))
favMovieList.append(str(input("Enter your second favorite movie name: ")))
favMovieList.append(str(input("Enter your third favorite movie name: ")))
print(favMovieList)

# 2) Question ka code
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1, "abc", "abc", 1]
list1 = ["m", "a", "a", "m",]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome") 
else:
    print("NOT Palindrome")

# 3) Question ka code 
# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# 4) Question ka code 
# Store the above values in a list & sort them from "A" to "D"

sortVal = ["C", "D", "A", "A", "B", "B", "A"]
print(sortVal.sort())
print(sortVal)

# ----------------- Side Practice -----------------

# Q1) Shopping List Manager
# User se 5 items ka naam input lo aur ek list me store karo.
# Phir:
# List print karo
# Last item ko pop() karke remove karo
# Ek naya item insert() karke index 2 pe daalo
# Final list print karo

finalList = []
finalList.append(str(input("Enter the first item name: ")))
finalList.append(str(input("Enter the second item name: ")))
finalList.append(str(input("Enter the third item name: ")))
finalList.append(str(input("Enter the fourth item name: ")))
finalList.append(str(input("Enter the fifth item name: ")))
print(finalList)

finalList.pop(-1) # Last item ko pop() karke remove karo
print(finalList)

finalList.insert(2, str(input("Enter new item on 2 index: "))) # Ek naya item insert() karke index 2 pe daalo
print(finalList) # Final List

# ----------------------------- Question one end -------------------------- 

# Q2) Even Number Filter
# Ek list banao jis me random numbers ho (tum khud daal do [2, 7, 8, 13, 20, 5]).
# Usme se sirf even numbers print karo.
# (Hint: for loop abhi nahi aaya, toh slicing ya indexing trick use karni padegi. Jahan loop lagta, wahan manually check karo har element ko if condition ke sath).

evenNumFilter = [2, 7, 8, 13, 20, 5]
for number in evenNumFilter:
    if number % 2 == 0:
        print(number, "is even number")
    else:
        print(number, "is not even number")

# ----------------------------- Question two end -------------------------- 

# Q3) Favorite Subjects Tuple
# Ek tuple banao apne 5 favorite subjects ka.
# Tuple ka length print karo
# Index 2 ka subject print karo
# Count karo kitni dafa "Math" aya hai

favSubject = ("Computer", "English", "Physics", "Maths", "History")
print(len(favSubject))
print(favSubject[2])
print(favSubject.count("Maths"))

# ----------------------------- Question three end -------------------------- 

# Q4) Mini Palindrome Test
# Ek string input lo user se (jaise "madam").
# Usko list me convert karo aur phir check karo ke palindrome hai ya nahi.
# (Hint: list() se string → list, phir reverse() compare karna jaise tumne pehle kiya).

userInp = str(input("Enter word: "))
charList = list(userInp)
copyList = charList.copy()
charList.reverse()
print(charList)

if charList == copyList:
    print("Palindrome")
else:
    print("Not Palindrome")

# ----------------------------- Question four end -------------------------- 

# Q5) Grade Analyzer
# Ek list banao = ["A", "C", "B", "A", "D", "B", "A", "C"]
# Phir:
# Count karo "A" kitni dafa aya
# List ko sort karo
# Last element print karo

grades = ["A", "C", "B", "A", "D", "B", "A", "C"]
print("Count of A:", grades.count("A"))
grades.sort()
print("Sorted Grades:", grades)
print("Last Grade in List:", grades[-1])

# ----------------------------- Question five end -------------------------- 
