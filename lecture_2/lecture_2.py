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
print(sliStr[:4]) 

# str[ starting_idx : ending_idx ] #ending idx is not included
# Accessing parts of a string

# str =

# “ApnaCollege”

# str[ 1 : 4 ] is “pna”

# str[ : 4 ] is same as str[ 0 : 4]

# str[ 1 : ] is same as str[ 1 : len(str) ]
