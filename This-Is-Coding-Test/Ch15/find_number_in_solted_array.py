# 입력값 받기
n, x = map(int, input().split())
array = list(map(int, input().split()))
l = 0
count = 0

while l <= n:
    mid = (l+n) // 2
    if array[mid] >= x:
        result = mid
        n = mid - 1
    else:
        l = mid + 1

while array[result] == x:
    count += 1
    result += 1

print(count)