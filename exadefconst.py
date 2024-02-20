#Example of default constructor :
class sample:
# default constructor
    def __init__(self):
        self.geek = "sample"
# a method for printing data members
    def print_Geek(self):
        print(self.geek)
# creating object of the class
obj = sample()
# calling the instance method using the object  'obj
obj.print_Geek()
'''Output :
sample'''
