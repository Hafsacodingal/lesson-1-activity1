seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def iterative(key):
    low = 0
    high = len(seats) - 1

    while low <= high:
        mid = (low + high) // 2
        if seats[mid] == key:
            return mid
        elif key < seats[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def recursive(low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if seats[mid] == key:
        return mid
    elif key < seats[mid]:
        return recursive(low, mid - 1, key)
    else:
        return recursive(mid + 1, high, key)

seat = int(input("Enter seat number: "))

print("Iterative:", iterative(seat))
print("Recursive:", recursive(0, len(seats) - 1, seat))