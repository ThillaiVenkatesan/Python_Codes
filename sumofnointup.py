n=int(input("enter the number of values:"))
tup=()
for i in range(0,n):
    a=int(input("enter the {} value:".format(i+1)))
    tup+=(a,)
j=0
s=0
while j<len(tup):
    s=s+tup[j]
    j+=1
print("sum of all numbers in tuple :",s)
