import math
class tri:
    a=0
    b=0
    c=0
    def side(self):
        a=int(input("Enter Side 1:"))
        b=int(input("Enter Side 2:"))
        c=int(input("Enter Side 3:"))
        s=a+b+c
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("THE AREA OF TRIANGLE:",area)
t=tri()
t.side()

