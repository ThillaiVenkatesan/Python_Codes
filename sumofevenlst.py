n=int(input("enter the number of values:"))
lst=[]
for i in range(0,n):
    a=int(input("enter the {} value:".format(i+1)))
    lst.append(a)
s=0
for a in lst:
    if a%2==0:
        s+=a
print("sum of even numbers in list:",s)
