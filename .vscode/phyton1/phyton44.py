n=3
print("===Counting Game Points with Multiplication(n=",n,"rounds)===")
print()

total=1 
steps=0
for round_num in range(1,n+1):
    total*=round_num
    steps+=1
print("Loop way :total=",total,"|steps=",steps)

total=1
nested_steps=0
for round_num in range(1,n+1):
    for point in range(1,round_num+1):
        nested_steps+=1

print()
print("Loop way : steps=",n)
print("Nested loop: steps=", nested_steps,"(grows much faster!)")
print()