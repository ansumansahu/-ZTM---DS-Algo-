# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# array1 = ['a', 'b', 'c', 'x']//array2 = ['z', 'y', 'i']
# should return false.
# -----------
# array1 = ['a', 'b', 'c', 'x']//array2 = ['z', 'y', 'x']
# should return true.

# 2 parameters - arrays - no size limit
# return true or false

#brute force O(mn) complexity (not optimal)
from genericpath import exists


def common(arr1,arr2):
    for i in arr1:
        for j in arr2:
            if i==j:
                return True
                break
    return False

print(common(['a','b','c'],['e','d']))

#another approach
#loop through arr1 and create object where properties is equal to items in arr
#loop through arr2 and check if items in 2nd array exists on created object
#so two seperate loops hence complexity reduces down to O(m+n)

def commonItems(arr1,arr2):
    d=dict()
    for i in range(len(arr1)):
        d[arr1[i]]=True
    
    for i in arr2:
        if i in d:
            return True
        return False 

print(commonItems(['a',1,'b'],[1,'c','d']))