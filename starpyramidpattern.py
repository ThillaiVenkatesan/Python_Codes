num=int(input("Enter A Value For Iteration:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print("*",end="")
    print()
