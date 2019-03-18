class main():
    def func(self,a):
        temp = a
        count = 0
        while(a!=0):
            r = a%10
            count = count+(r*r*r)
            a = a//10
        if (count==temp):
            print("yes")
        else:
            print("no")
ob = main()
a=int(input())
ob.func(a)
