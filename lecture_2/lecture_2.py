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