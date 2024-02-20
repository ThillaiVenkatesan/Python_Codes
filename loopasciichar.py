rows=int(input("Enter the Row Value"))
a=65
for i in range(0,rows):
    for j in range(0,i+1):
        val=chr(a)
        print(val,end=" ")
    a+= 1 
    print()
