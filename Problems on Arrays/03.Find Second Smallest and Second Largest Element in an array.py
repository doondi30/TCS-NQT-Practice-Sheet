arr = [5, 3, 8, 1, 9, 2]
arr.sort()
small = arr[1]
large = arr[-2]

print("Second smallest is", small)
print("Second largest is", large)

#optimal

def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small
