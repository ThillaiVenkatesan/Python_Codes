def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) +fibonacci(n-2))    
n= int(input("ENTER THE NUMBER OF TERMS:"))  
if n<= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(fibonacci(i))  
