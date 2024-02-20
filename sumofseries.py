#Write a program to sum the series:1/1 + 22 /2 + 33 /3 + ……. nn/n
n = int(input("Enter a value of n: "))
s=0.0
for i in range(1,n+1):
    a=float(i**i)/i
    s=s+a
print("The sum of the series is ", s)
