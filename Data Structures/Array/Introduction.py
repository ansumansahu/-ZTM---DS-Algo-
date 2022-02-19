strings=['a','b','c','d']

# Look-up/Acces
print(strings[2]) #Time O(1)

# Push/Pop 
# append to list in python
strings.append('e') #Adds 'e' at the end of the array in O(1) time
print(strings)
# Pops/removes the element at the end of the array in O(1) time
strings.pop() 
strings.pop()
print(strings)

# Insert
# inserts an element at beginning of array, or any location specified
# this shifts all other elements one place towards right
# This requires looping through the array. Hence, O(n) time
strings.insert(0,'x')
print(strings)

# Delete
# deletes an element from the specified location in O(n) time
# pop(index) or remove(item) or del - All O(n)
strings.pop(0) #deletes item at index=0
strings.remove('a') #removes 1st occurence of item
del strings[0:1] #delete a range
print(strings)