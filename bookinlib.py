#Program 2:write a menu driven program that keeps record of books available in you school library
class Library:
    def __init__(self):
        self.bookname=""
        self.author=""
    def getdata(self):
        self.bookname = input("Enter Name of the Book: ")
        self.author = input("Enter Author of the Book: ")
    def display(self):
        print("Name of the Book: ",self.bookname)
        print("Author of the Book: ",self.author)
        print("\n")
book=[] #empty list
ch = 'y'
while(ch=='y'):
    print("1. Add New Book \n 2.Display Books")
    resp = int(input("Enter your choice : "))
    if(resp==1):
        L=Library()
        L.getdata()
        book.append(L)
    elif(resp==2):
        for x in book:
            x.display()
    else:
        print("Invalid input....")
    ch = input("Do you want continue....")
'''Output:
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: Programming in C++
Enter Author of the Book: K. Kannan
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: Learn Python
Enter Author of the Book: V.G.Ramakrishnan
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: Advanced Python
Enter Author of the Book: Dr. Vidhya
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: Working with OpenOffice
Enter Author of the Book: N.V.Gowrisankar
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: Data Structure
Enter Author of the Book: K.Lenin
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 1
Enter Name of the Book: An Introduction to Database System
Enter Author of the Book: R.Sreenivasan
Do you want continue....y
1. Add New Book
2.Display Books
Enter your choice : 2
Name of the Book: Programming in C++
Author of the Book: K. Kannan
Name of the Book: Learn Python
Author of the Book: V.G.Ramakrishnan
Name of the Book: Advanced Python
Author of the Book: Dr. Vidhya
Name of the Book: Working with OpenOffice
Author of the Book: N.V.Gowrisankar
Name of the Book: Data Structure
Author of the Book: K.Lenin
Name of the Book: An Introduction to Database System
Author of the Book: R.Sreenivasan
Do you want continue....n'''
