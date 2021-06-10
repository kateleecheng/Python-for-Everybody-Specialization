#Week_5_Class.py

purse=dict()
purse['money']=12 #money is the label of 12
purse['candy']=3
purse['tissue']=75
print(purse)
#{'money': 12, 'candy': 3, 'tissue': 75}
print(purse['candy'])
#3
purse['candy']=purse['candy']+2
print(purse)
#{'money': 12, 'candy': 5, 'tissue': 75}

#list is position
#distionary is label

lst=list()
lst.append(21)
lst.append(183)
print(lst)
#[21, 183]
lst[0]=23
print(lst)
#[23, 183]

ddd=dict()
ddd['age']=21
ddd['course']=182
print(ddd)
#{'age': 21, 'course': 182}
ddd['age']=23
print(ddd)
#{'age': 23, 'course': 182}
