import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(1000)] #increase the range accordingly

def find_nemo(array):
    t0 = time.time()
    for i in range(0,len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')

find_nemo(nemo)
find_nemo(everyone)
find_nemo(large) 
#O(n)--> Linear Time
#no of operations increase linearly with increase in no of elements