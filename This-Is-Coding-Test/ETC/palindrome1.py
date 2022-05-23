# n ~ m 사이 자연수 중 팰린드롬인 숫자의 개수
n, m = map(int, input().split())

def palindrome(word):
    for i in range(0, len(word) // 2):
        if word[i] == word[-i -1]:
            continue
        else:
            return False
    return True


def solution(n, m):
    answer = 0
    for num in range(n, m):
        if palindrome(str(num)):
            answer += 1
    return answer

solution(n, m)