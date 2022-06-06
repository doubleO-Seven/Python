'''a = 0
b = int(input("Enter the last range: "))
for i in range (a, b+1):
    print(i)
'''
#print even odd in a range
a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))

for i in range(a, b):
    if i%2 !=0:
        print(i, end=' ')