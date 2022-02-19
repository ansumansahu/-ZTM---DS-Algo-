# Building our own array data structure
class myArr():
    def __init__(self):
        self.length=0
        self.data={}
    
    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data[self.length]=item #Adds the item to the end of array
        self.length+=1 #Increment the length by 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1] #Collects the last element
        del self.data[self.length - 1] #Deletes the last item of the array
        self.length -= 1 #Decrement the length by 1
        return last_item #Returns the popped element O(1)

    def delete(self,index):
        self.item=self.data[index]
        self.shiftitems(index)
    
    def shiftitems(self,index):
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

new_arr = myArr()
new_arr.push('data')
new_arr.push('structures')
new_arr.push('and')
new_arr.push('algorithms')
print(new_arr.data)
# {0: 'data', 1: 'structures', 2: 'and', 3: 'algorithms'}

print(new_arr.pop()) # algorithms
print(new_arr.data)
# {0: 'data', 1: 'structures', 2: 'and'}

new_arr.delete(2)
print(new_arr.data)
# {0: 'data', 1: 'structures'}