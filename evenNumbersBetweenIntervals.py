a,b = input().split()
a = int(a)
b = int(b)+1
for i in range (a,b):
    if (i%2==0):
        print (i,end=' ')
