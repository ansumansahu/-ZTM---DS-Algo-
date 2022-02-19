def RevStr(s):
    rev_str=''
    for char in range(len(s)-1,-1,-1): #O(n)
        rev_str+=s[char]
    return rev_str

s=input() 
print(RevStr(s)) 
#since we are creating new array of same size, space complexity is O(n)

#Built-In Functions For the same
s1='Data'
print(s1[::-1])  #O(n)

s2='Array'
print(''.join(reversed(s2))) #O(n)