#Week_1_Asm.py
text = "X-DSPAM-Confidence:    0.8475"
spacepos=text.find(' ')
#print(spacepos)

#print(text[spacepos:])
#print(text[spacepos:].lstrip())

ftext=float(text[spacepos:].lstrip())
print(float(ftext))
