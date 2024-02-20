#classoddeven
class odd_even:
    even=0
    def check(self,num):
        if num%2==0:
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
n=odd_even()
x=int(input("Enter A Value:"))
n.check(x)
