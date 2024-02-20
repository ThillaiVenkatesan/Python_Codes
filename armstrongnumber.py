num=int(input("enter a positive number"))
s=0
temp=num
while temp>0:
    digit=temp%10
    s+=digit**3
if num==s:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
