#Week_5_Asm.py
hrs=input('Enter Hours:')
rate=input('Enter Rate:')

f_hrs=float(hrs)
f_rate=float(rate)

Pay=f_hrs*f_rate

if f_hrs>40:
    Pay=40*f_rate+(f_hrs-40)*f_rate*1.5
print(Pay)

score=input('Enter Score:')
try:
    sc=float(score)
except:
    sc=-1
if sc==-1:
    print('Error')
elif sc>1:
    print('Error')
elif sc<0:
    print('Error')
elif sc>=0.9:
    print('A')
elif sc>=0.8:
    print('B')
elif sc>=0.7:
    print('C')
elif sc>=0.6:
    print('D')
elif sc<0.6:
    print('F')
