n=int(input("number of elements in the tuple"))
tup=()
for i in range(0,n):
    num=int(input("entr the {} value".format(i+1)))
    tup+=(num,)
a=max(tup)
print("maximum value in tup",a)
