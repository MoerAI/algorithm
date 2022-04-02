import math

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
     array.append(int(input()))
array.sort()

dis = array[-1] - array[0]

print(dis)

print(math.ceil(dis/c))