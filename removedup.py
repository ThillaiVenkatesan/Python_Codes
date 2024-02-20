n=int (input("enter no. of elements"))
lst=[]
for i in range(0,n):
    a=int(input("enter the element"))
    lst.append(a)
j=0
while j<len(lst):
    c=lst.count(lst[j])
    if c>1:
        del lst[j]
    else:
        j+=1
print("list elements after removing duplicates is",lst)
