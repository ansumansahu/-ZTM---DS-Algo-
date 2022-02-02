#5 Space complexity O(1)
def jumpscare(n):
    for i in range(len(n)): 
        print('boo!!!')
    
jumpscare([1,2,3,4,5]) #O(1)

#6 Space complexity O(n)
def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(n):
        hiArray.append('hi')
    
    print(hiArray)

arrayOfHiNTimes(5) #O(n)