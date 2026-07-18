scores = [45, 67, 89, 72, 90]

def direct(index):
    print(scores[index])

def search(score):
    if score in scores:
        print("Found")
    else:
        print("Not Found")

def compare():
    for i in scores:
        for j in scores:
            print(i, j)

print("1. Direct")
print("2. Search")
print("3. Compare")

choice = input("Enter choice: ")

if choice == "1":
    index = int(input("Enter index: "))
    direct(index)

elif choice == "2":
    score = int(input("Enter score: "))
    search(score)

elif choice == "3":
    compare()