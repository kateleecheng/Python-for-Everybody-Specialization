#

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends=['Joseph','Glenn','Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

print('Before')
for thing in[9,41,12,3,74,15]:
    print(thing)
print('After')

#largest
largest_so_far=-1
print('Before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far)
print('After', largest_so_far)

#Counting
zork=0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork, thing)
print('After', zork)

#Sum
zork=0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+thing
    print(zork, thing)
print('After', zork)

#Average
count=0
sum=0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count+1
    sum=sum+value
    print(count, sum, value)
print('After', count, sum, sum/count)

print('Before')
for value in [9,41,12,3,74,15]:
    if value>20:
        print ('Large number',value)
print('After')

found=False
print('Before',found)
for value in [9,41,12,3,74,15]:
    if value ==3:
        found=True
    print(found,value)
print('After',found)

smallest=None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('After', smallest)
