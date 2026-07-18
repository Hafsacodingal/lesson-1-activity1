# Running Lap Tracker

laps = int(input("Enter number of laps: "))

# Method 1: Formula
points1 = laps * 1
print("Formula:", points1)

# Method 2: Loop
points2 = 0
for i in range(laps):
    points2 += 1
print("Loop:", points2)

# Method 3: Nested Loop
points3 = 0
for i in range(laps):
    for j in range(1):
        points3 += 1
print("Nested Loop:", points3)

# Complexity
print("\nTime Complexity")
print("Formula = O(1)")
print("Loop = O(n)")
print("Nested Loop = O(n)")

print("\nSpace Complexity")
print("Formula = O(1)")
print("Loop = O(1)")
print("Nested Loop = O(1)")

print("\nMost Efficient: Formula Method")