n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
m = min(n1,n2)
while(1):
  if(m % n1 == 0 and m % n2 == 0):
     print("LCM of two number is: ", m)
     break
  m += 1
