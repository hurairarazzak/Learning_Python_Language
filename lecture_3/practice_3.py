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

fruits = ["apple", "banana", "mango"]
print("Original List:", fruits)

fruits.append("orange")
print("After Append:", fruits)

fruits.remove("banana")
print("After Remove:", fruits)

numbers = (2, 4, 6, 8, 10)
print("Tuple:", numbers)
print("First three numbers:", numbers[0:3])
print("Count of 2 in tuple:", numbers.count(2))
