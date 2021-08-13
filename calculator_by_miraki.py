def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def divide(a,b):
    c=a/b
    print(c)
def floor_division(a,b):
    c=a//b
    print(c)
def modulus(a,b):
    c=a%b
    print(c)
def main(a,b):
    if sym=="add":
        add(a,b)
    elif sym=="sub":
        sub(a,b)
    elif sym=="mul":
        mul(a,b)
    elif sym=="divide":
        divide(a,b)
    elif sym=="floor_division":
        floor_division(a,b)
    elif sym=="modulus":
        modulus(a,b)
    else:
        pass
sym=input("enter sym=")
a=int(input("Enter the any number"))
b=int(input("Enter the any number"))
main(a,b)
    