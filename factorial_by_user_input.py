x=int(input("Enter number"))
def factorial(x):
	if x==0 or x==1:
         return 1
	else:
	    return x*factorial(x-1)
print(factorial(x))