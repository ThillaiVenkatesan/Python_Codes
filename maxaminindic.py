#10. Write a program that prints the maximum and minimum value in a dictionary.
a={1:45,2:58,3:66,4:12,5:4}
print(a)
b=max(a, key = lambda x: a.get(x) )
c=min(a, key = lambda x: a.get(x) )
print("the maximum in the given dictionary ",a[b])
print("the minimum in the given dictionary ",a[c])
#Output:
#{1: 45, 2: 58, 3: 66, 4: 12, 5: 4}
#the maximum in the given dictionary 66
#the minimum in the given dictionary 4
