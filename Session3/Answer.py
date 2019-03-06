# A nested list is a list that appears as an element in another list. 
# In this list, the element with index 3 is a nested list. 
# If we print(nested[3]), we get [10, 20]. 
# To extract an element from the nested list, we can proceed in two steps. 
# First, extract the nested list, then extract the item of interest. 
# It is also possible to combine those steps using bracket operators that evaluate from left to right.
nested = ["hello", 3.0, 5, [10, 20,30]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][2])
# ---------------------------------------------------------------------------------------------------------
#Yes, list can store both integers and strings in it
ls = ["Hello",50]
print(ls)