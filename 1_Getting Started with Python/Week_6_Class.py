#Week_6_Class.py
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

big=max('Hello world')
print(big)

print (float(99)/100)
i=42
type(i)
f=float(i)
print(f)
type(f)
print(1+2*float(3)/4-5)

x=5
print('Hello')

def print_lyrics():
    print("XXX")
    print('YYY')
print('Yo')
print_lyrics()
x=x+2
print(x)

def greet(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

def greet1(lang1):
    if lang1 == 'es':
        return 'Hola'
    if lang1 =='fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet1('en'),'Gleen')
print(greet1('es'),'Sally')
print(greet1('fr'),'Michael')

def addtwo(a,b):
    added=a+b
    return added

x=addtwo(3,5)
print(x)

def stuff():
    print('Hello')
    return
    print('World')

stuff()
