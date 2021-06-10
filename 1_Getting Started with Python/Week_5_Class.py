#Week_5_Class.py
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
if x == 5:
    print('Equal 5')
if x >= 5:
    print('Freater than or equal 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')
print('Finis')

x=5
if x>2:
    print('Bigger thatn 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i>2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

x=42
if x>1:
    print('More than one')
    if x<100:
        print('Less than 100')
print('All done')

x=4
if x>2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

if x<2:
    print('small') #x=0
elif x<10:
    print('Medium') #x=5
else:
    print('Large') #x=20
print('All done')

astr='Hello Bob'
try:
    istr=int(astr)
except:
    istr=-1
print('First', istr)

astr ='123'
try:
    istr=int(astr)
except:
    istr=-1
print('Second', istr)

astr='Bob'
try: #safety nest
    print('Hello')
    istr=int(astr)
    print('There')
except:
    istr=-1
print('Done', istr)

rawstr=input('Enter a number:')
try:
    ival=int(rawstr)
except:
    ival=-1

if ival>0:
    print('Nice work')
else:
    print('Not a number')
