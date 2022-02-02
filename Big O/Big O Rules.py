# 1. Worst Case
arr=[1,2,3,4,5,6,7,8,9,10]
def find(input):
    for i in range(len(input)):
        if i==5:
            print('Found 5')

find(arr)
# Time Complexity is O(n) because even though 5 is found half way
# we assume worst case scenario gor Big O notation

# 2. Remove Constants
import math
def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])                         #O(1)
    
    middleIndex=math.floor(len(items)/2)    
    index=0                                 
    while(index<middleIndex):               
        print(items[index])                 #O(n/2)
        index+=1                            
    
    for i in range(100):                    
        print('Hi')                         #O(100)

# Big O of the function would be O(1+n/2+100) so acc to rule2 we remove all
# constants because those won't affect much and overally Big O is O(n)

# 3. Different terms of inputs:
# For nested loops, Big O Notation is O(n^2) - Quadratic Time

# 4. Drop Non-Dominants
# O(n+n^2) becomes O(n^2)