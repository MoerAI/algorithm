# 브루트 포스 방식
def solution1(n:int, m:int) -> int:
    answer = 0
    while n > 0:
        answer += 1
        n -= 1
        if(answer % m == 0):
            n += 1
    
    return answer

# 사칙연산
def solution(n:int, m:int) -> int:
    if( m == 2):
        answer = n * m - 1    
    else:
        answer = n/m + n + 1
    return int(answer)

# 변태처럼
def solution2(n:int, m:int) -> int:
    return int(n * m - 1 if  m == 2 else n/m + n + 1)
print(solution1(11,5))
print(solution(11,5))
print(solution2(11,5))