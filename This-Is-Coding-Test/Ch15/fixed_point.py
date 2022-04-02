n = int(input())
array = list(map(int, input().split()))
l = 0

while(l <= n):
    middle = (l+n) // 2
    if array[middle] == middle:
        print(middle)
        break
    elif array[middle] > middle:
        n = middle - 1
    else:
        l = middle + 1