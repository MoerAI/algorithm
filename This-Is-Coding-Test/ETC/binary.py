# 자연수 n을 이진법으로 변환했을 때 나오는 1의 개수를 k라고 했을때,
# n보다 작은 자연수 중에서 이진법으로 변환하여 1의 개수가 k인 수가 몇 개 있는지를 return 하도록 하라
import math
import time

def solution(n):
    start = time.time()
    bi = bin(n)
    k = bi.count("1")
    length = len(bi) - 2
    result= 1
    div = 1
    count = 0
    mx = 2 ** (length)
    result = int(result/div)

    # 이 부분을 경우의 수로 만들면 더 빠르게 처리 할 수 있음
    for i in range(n, mx):
        if bin(i).count("1") == k:
            count += 1

    for _ in range(k):
        result = length * result
        div = k * div
        length = length -1
        k = k - 1
    
    end = time.time()
    return int((result/div) - count), print(f"{end - start:.5f} sec")

# 2의 30승 1,073,741,824
solution(1063740024)
solution(9)
solution(100)
# 0011
# 0101
# 1001
# 1010
# 1100
# 0110
