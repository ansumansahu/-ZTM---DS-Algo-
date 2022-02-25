def Hi():
    return 'Hi'
user={
    'age':30,
    'name':'Tarik',
    'magic':True,
    'intro': Hi()
}

print(user,user['age'])
print(user.keys(),user.values(),user.items())