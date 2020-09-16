from typing import List
def solution(grade: List[int], max_diff:int) -> int:
    grade.sort()
    answer = []
    if max_diff == 1:
        return 1
    for person in grade:
        group_max_score = person + max_diff
        team = 0
        for i in range(person, group_max_score + 1):
            if i in grade:
                team = team + grade.count(i)
        answer.append(team)
        
    return max(answer)

#딕셔너리 이용
def solution2(grade: List[int], max_diff:int) -> int:
    grades = {}
    answer = []
    max_grade = max(grade)
    for score in grade:
        try: grades[score] += 1
        except: grades[score] = 1
    key = list(grades.keys())
    for k in key:
        team = 0
        group_max_score = k + max_diff
        for i in range(k, group_max_score + 1):
            if(i in key):
                team += grades[i]
        answer.append(team)
    return max(answer)

def solution3(grade: List[int], max_diff:int) -> int:
    grades = {}
    answer = []
    team = 0
    max_grade = max(grade)
    for score in grade:
        try: grades[score] += 1
        except: grades[score] = 1
    key = list(grades.keys())
    max_key = max(key)
    for i in range(0, max_key + 1):
        if(i in key):
            team += grades[i]
        if(i - max_diff - 1 in key):
            team -= grades[i - max_diff - 1]
        answer.append(team)
    return max(answer)
print(solution3([4,1,3,5],2))