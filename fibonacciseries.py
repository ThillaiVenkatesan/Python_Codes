num=int(input("Enter a number:"))
a,b=-1,1
c=0
print ("the fibonacci series upto",num)
while c<=num:  
    print(c)
    a=b
    b=c
    c=a+b
    
