lst = [1,2,3,4,78.9,45.5,"mrinal tripathi",False]
print(lst[3])
lst2 = [1,2,3.5,6,[5,6,7,9]]
print(lst2[4][2])

lst3 = lst + lst2
print(lst3)

lst4 = [1,2,3] * 4
print(lst4)

for i in lst3:
    print(i)
    
for i in lst4:
    print(i)
    
print(1 in lst2)

print(1 not in lst2)