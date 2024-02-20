mark1=int(input("enter your mark1:"))
mark2=int(input("enter your mark2:"))
avg=mark1+mark2/2
if avg>=80:
    print("you have got A grade")
elif avg>=70and avg<80:
    print("you have got B grade")
elif avg>=60and avg<70:
    print("you have got C grade")
elif avg>=50and avg<60:
    print("you have got D grade")
else:
    print("you have got E grade")
# in elif we can give condition without and part as that condition is previously checked
