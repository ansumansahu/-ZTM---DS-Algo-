import time

nemo=['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large=['nemo' for i in range(1000)]

def findNemo(arr):
    t0= time.time()
    for i in range(len(arr)):
        if arr[i]=='nemo' :
            print("Found Nemo!!")
    t1= time.time()
    print(f'Time taken :{t1-t0} ms')

#with increase in array size time taken for the loop is also increases
findNemo(large)