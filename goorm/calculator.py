def solution(n, m):
    sum = 0
    for i in range(n, m + 1):
        s = str(i)
        l = list(s)
        mul = 1
        for c in l:
            mul = mul * int(c)
        sum += mul
    return sum


solution(15, 25)
solution(10, 20)
solution(10, 100)