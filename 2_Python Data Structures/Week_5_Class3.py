#Week_5_Class3.py

counts=dict()
print('Enter a line of the text')
line=input('')

words=line.split() #split into list of words

print('Words:', words)

print('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts',counts)

counts={'chuck':1, 'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])

jjj={'chuck':1, 'fred':42,'jan':100}
print(list(jjj))
#['chuck', 'fred', 'jan']
print(jjj.keys())
#dict_keys(['chuck', 'fred', 'jan'])
print(jjj.values())
#dict_values([1, 42, 100])
print(jjj.items())
#dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])

for aaa,bbb in jjj.items():
    print(aaa,bbb)
