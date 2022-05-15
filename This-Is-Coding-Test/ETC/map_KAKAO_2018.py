def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        low = ""
        map = bin(arr1[i] | arr2[i])
        if len(map) != n + 2:
            for _ in range(n+2-len(map)):
                map = map[:2] + "0" + map[2:]
        for m in map[2:]:
            if m == '1':
                low = low + "#"
            if m == '0':
                low = low + " "
        answer.append(low)
        
    return answer