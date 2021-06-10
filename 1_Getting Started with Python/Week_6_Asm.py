#Week_6_Asm.py

hrs=input('Enter Hours:')
rate=input('Enter Rate:')

f_hrs=float(hrs)
f_rate=float(rate)

def computepay(f_hrs,f_rate):
    if f_hrs>40:
        Pay=40*f_rate+(f_hrs-40)*f_rate*1.5
    else:
        Pay=f_hrs*f_rate
    return Pay
p=computepay(f_hrs,f_rate)
print("Pay", p)
