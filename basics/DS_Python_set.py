# set is the collection of unordered, unchangeable, and unindexable items
# set is mutuable data type, because we can add or remove items from set
# but set elements are immutable because we cannt change items after creation but can add more items.
# set elements stored in curly braces. 
# every items separated by comma.
# set contain only immutable data type elements like interger, string etc

st = {1,2,3,4,5,6}
st1 = {3,4,5,6,7,8,17,89}
st2 = st.symmetric_difference(st1)
st2 = st.difference(st1)
st2 = st.union(st1)
st2 = st.intersection(st1)
print(st2)

for i in st:
    print(i)