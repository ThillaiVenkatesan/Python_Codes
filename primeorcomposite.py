num=int(input("Enter Any Positive Number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is a composite number")
            break
    else:
        print(num,"is a prime number")
elif num==1:
    print(num,"is neither prime nor composite")
else:
    print(num,"is an invalid input")
