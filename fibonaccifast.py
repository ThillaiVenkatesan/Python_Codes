from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n)!=int:
        print("please enter a positive integer")
    if n<1:
        print("please enter a positive integer")
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
for n in range(1,101):
    print(n,":",fibonacci(n))