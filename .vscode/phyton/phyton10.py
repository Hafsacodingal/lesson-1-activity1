num= 10 
for i in range(0, 11):
    print("5*",i,"=",5*i)

n=int(input("Enter numbers of rows you want ?")) 
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ") 
    print()       

num=int(input("Enter a numbers:"))
if num >1:
    for i in range(2,int(num**0.5 +1)):
       if num%i==0:
           print(f"{num}is not a prime number." )
           break
    else:
        print(f"{num}is  a prime number." )
else:
    print(f"{num}is not a prime number." )  

total_sum=0
num=1
while num<=10:
     total_sum+=num
     num+=1
print(f"The sum of the first ten natural numbers is {total_sum}")          