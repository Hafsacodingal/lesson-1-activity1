def intro(name):
    print("Hello,Good morning!I am", name)
user_name= input("Enter your name")
intro(user_name)

def recur_factorial(n):
    if n==1:
       return n
    else:
        return n*recur_factorial(n-1)
num=int(input("Enter a number"))
if num <0:
    print("Sorry,factorial does not exist for negative numbers")
elif num ==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,recur_factorial(num))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print(add(4,5))
print(sub(7,5))
print(mul(4,7))
print(div(2,6))