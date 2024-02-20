'''a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
if a<b:
      if a<c:
        print (a,"is minimum of three numbers")
      else:
        print (c,"is minimum of three numbers") 
       
elif b<c:
       print (b,"is minimum of three numbers")
else:
        print(c,"is minimum of three numbers")'''
#maximum of three is down program
a= int(input("Enter number 1"))
b= int(input(" Enter number 2"))
c= int(input(" Enter number 3"))
if a > b and a > c:
      print(" A is greatest")
elif b > a and b > c:
      print("B is greatest")
else:
      print("C is greatest")
