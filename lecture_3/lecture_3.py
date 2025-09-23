# marks1 = 94.7
# marks2 = 82.3
# marks3 = 67.4
# marks4 = 75.5
# marks5 = 64.8
# Agr is tareqe se 50 students ko add karna hoga tou 50 variable bnane honge
# tou is tareqe se bht zyada variable bnane honge aur har var.. ko track karna hoga

marks = [84.2, 76.1, 97.6, 85.4, 98.3]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[2])

student = ["Ali", 84, "Karachi"] # we can also store different types of data
print(student)

student[0] = "Huraira" # Allowed in python
# print(student)

# List Slicing
# list_name[ starting_idx : ending_idx ] #ending idx is not included
# Similar to String Slicing

firstmarks = [86, 45, 79, 82, 93]
print(firstmarks[2:4])

secondMarks = [96, 65, 45, 76]
print(secondMarks[-3:-1])

# List Methods
numList = [2, 1, 3]
print(numList.append(4))
print(numList.sort()) #sorts in ascending order
# print(numList.sort(reverse = True)) #sorts in descending order
print(numList)

list = ["banana", "litchi", "apple"]
# print(list.append(4))
print(list.sort())  #sorts in ascending order
# print(list.sort(reverse = True)) #sorts in descending order
print(list)

alphaList = ["a", "d", "e", "f", "c", "b"]
print(alphaList.sort(reverse = True)) # ab descending mae hona yae chaye kae b, c, f aese start 
# hou but yae aese nhi hoga kiyu keye string ke first charcter ke hisaab se sort hota hae tou ab
# descending ulte alphabet count honge tou isme last f hae tou f se shuru hoga phir e phir d aese hoga
# aur ascending mae string ka alpabet jou pehle aate hae wou waha se start honge aese means smjhna 
# yae hae kae forward and backward sirf nhi hae jou character alphabet honge us hisaab se sort hote hae
print(alphaList)

alpList = ["g", "f", "t", "j", "e", "b"]
alpList.reverse() # ab ye method poori list ko palt dega aur yae original list ke andar change
# karta hae isme first chr wala scene nhi hae yae poori list plat dega last wale pehle ayenge 
# and pehle wale end mae
print(alpList)

fruitList = ["apple", "banana", "grape"]
fruitList.insert(2, "cherry") #insert element at index
print(fruitList)

pyList = [1, 2, 5, 4]
pyList.remove(5) #removes first occurrence of element
print(pyList)

popList = ["David", "Huraira", "Saif", "Raeed"]
popList.pop(2) #removes element at idx
print(popList)

# Tuples in Python
# A built-in data type that lets us create immutable sequences of values.

tup = (2, 1, 3, 1)
print(tup[0])
print(tup[1])
# tup[0] = 5 # Not allowed bcz tupple is immutable

# tupl = (1,) # , is compulsory in tuple in the end if the value lenght is one if we didn't put , the
# python will predict that the value is integer or float and string etc, and in the case of multiple
# value like if we have the three length in tuple so it is not necesaary to put , in the end or 
# incase you put it so that not an issue it's depend on you if you want to put or leave both is correct

# tupl = () # we can also create empty tuple
tupl = (1, 2, 3, 4)
print(tupl[0:2]) # Slicing in tuple
print(type(tupl))

# Tuple Method
numTuple = (2, 1, 3, 1, 2, 2)
print(numTuple.index(3)) # Output: 2 bcz in the tuple the 3 is in index 2, also returns index of
# first occurrence if the element is not found, it will raise an error. 

print(numTuple.count(2)) # Output is 3 bcz the count will find that how many 2 is in your tuple
# and in numTuple there are 3 tuples if the element is not found it will raise 0
