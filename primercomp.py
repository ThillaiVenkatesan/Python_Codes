b=list(range(1,101))
c,d=[],[]
for i in b:
    a=0
    if i==1:
        print("it is neither prime nor composite:",i)
    for j in range(2,i):
        if i%j==0:
            c.append(i)
            a=1
            break
    if a==0 and i!=1:
        d.append(i)
print("the prime numbers are:",d)
print("the composite numbers are:",c)

