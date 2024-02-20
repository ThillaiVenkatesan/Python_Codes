#pg(program)1:Write a program to calculate area and circumference of a circle
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*(self.radius**2)
    def circumference(self):
        return 2*Circle.pi*self.radius
r=int(input("Enter Radius: "))
C=Circle(r)
print("The Area =",C.area())
print("The Circumference =", C.circumference())
'''Output:
Enter Radius: 5
The Area = 78.5
The Circumference = 31.400000000000002
Program'''
