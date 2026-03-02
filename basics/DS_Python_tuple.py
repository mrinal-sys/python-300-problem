# tuple is a data type used in python
# tuple is immutable data type, we cannt change tuple items after creation
# tuple contain multiple values having different data types
# tuple is the ordered data structure having a sequence in items / elements
# tupe stored elements/ items closed with parenthesis 
# we can create  a tuple another tuple, as nested tuple

tuple = (2,3,45,6.7,"Mrinal",True)
print(tuple[4])

tuple1 = (3,6,7,8,9.0,4.5,("Raghav", True))
print(tuple1[6][1])

tuple3 = tuple + tuple1
print(tuple3)

tuple4 = (1,2,3) * 5
print(tuple4)

# memebership operator 
print(2 in tuple)
print('Mrinal' in tuple)

# iterating 
for i in tuple:
    print(i)