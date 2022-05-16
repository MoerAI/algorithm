def solution(N, stages):
    # 스테이지 카운트
    stage_count = []
    for i in range(1, N + 1):
        stage_count.append(stages.count(i))
    num = len(stages)

    # 각 스테이지 실패율 구하기
    fail = []
    for i in range(N):
        if num != 0:
            fail.append(stage_count[i]/num)
            num = num - stage_count[i]
        elif num == 0:
            fail.append(0)

    # 실패율 내림차순으로 뽑기
    answer = []
    for i in range(N):
        max_index = fail.index(max(fail))
        answer.append(max_index + 1)
        fail[max_index] = -1
        
    return answer