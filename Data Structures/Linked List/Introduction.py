# Generic linked list view: 
# apples 
# 8947 -> grapes 
#         8742 -> oranges
#                 3742 -> Null

# Understanding Pointer
dict1={
    'a':"ansh"
}
dict2=dict1
# we are not creating aanother memory space storing the same thing
# instead both dict point to the same memory allocation 
dict1["a"]="sahu"
# changing the value will be reflected for both cases
print(dict1["a"])
print(dict2["a"])