# mutable and immutable
# list is a example of mutable data type where can be modified 
# in place after the object is created — without changing its identity (id() remains the same).
lst = [2,4,5,6,7]
lst[2] = 98
print(lst)

tple = (2,4,6,7,8,9,0)
print(tple[3])
# TypeError: 'tuple' object does not support item assignment

# sequence and non sequence data type
str = "Mrinal Tripathi"
print(str[3])
# lst, tple, str is a example of sequence data type

# in set data type elements are not stored in a well organised form below is the 
# example

set = {2,4,5,6,7,8,0}
# print(set[4])
# TypeError: 'set' object is not subscriptable
print(set)