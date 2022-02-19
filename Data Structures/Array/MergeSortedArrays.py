from numpy import sort


def merge(arr1,arr2):
    new_arr=[]
    for i in arr1:      #O(n) 
        arr2.append(i)
    return sort(arr2)   #O(nlogn)

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(merge(arr1,arr2))

# def merge_sort(arrA, arrB):
#     new_arr = []
 
#     while len(arrA) and len(arrB):
#         if arrA[0] < arrB[0]:
#             new_arr.append(arrA[0])
#             arrA.pop(0)
#         else:
#             new_arr.append(arrB[0])
#             arrB.pop(0)
 
#     return [*new_arr, *arrA, *arrB]