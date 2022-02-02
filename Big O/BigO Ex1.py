nemo=['nemo' for i in range(1000)]

def funChallenge(input): 
    a=10                        #O(1)
    a=50+3                      #O(1)
    for i in range(len(input)): #O(n)
        stranger=True           #n*O(1) -> O(n)
        a+=1                    #n*O(1) -> O(n)
    return a                    #O(1)

funChallenge(nemo)

# So the overall time complexity would be O(3+3n) which would be equal to O(n)