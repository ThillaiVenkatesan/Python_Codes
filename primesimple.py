n=int(input("Enter A  Positive Number:"))
if n==1:
    print("it is neither prime or composite")
elif all(n%i!=0 for i in range(2,n)):
    print ("it is prime number")
else:
    print("it is composite")
