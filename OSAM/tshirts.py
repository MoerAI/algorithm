from typing import List

# 브루트 포스 방식
def solution(people: List[int], tshirts: List[int]) -> int:
    people.sort()
    tshirts.sort()
    answer = 0
    for person in people:
        for shirt in tshirts:
            if(person <= shirt):
                answer += 1
                tshirts.remove(shirt)
                break
    return answer

# 같은 녀석들을 먼저 제거
def solution2(people: List[int], tshirts: List[int]) -> int:
    people.sort()
    tshirts.sort()
    answer = 0
    
    for person in people:
        if(person in tshirts):
            people.remove(person)
            tshirts.remove(person)
            answer += 1
            
    for person in people:
        if(person > min(tshirts)):
            tshirts.remove(min(tshirts))
        else:
            people.remove(person)
            tshirts.remove(min(tshirts))
            answer += 1
    return answer

print(solution([1,2,3,3,3,3,3,3,4,5,6,7,8,25],[1,1,2,2,3,5,7,10,11,15,17,20,30]))