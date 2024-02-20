n=int(input("Enter the  number of elements:"))
lst=[]
for i in range(0,n):
    a=int(input("enter the {} elment".format(i+1)))
    lst.append(a)
rev=[]
c=len(lst)
j=c-1
while j>=0:
    rev.append(lst[j])
    j-=1
print("reversed lst:",rev)
