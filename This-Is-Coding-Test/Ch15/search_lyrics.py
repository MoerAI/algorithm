def solution(words, queries):
    for querie in queries:
        for word in words:
            result = 0
            # 문자열 길이 확인
            if len(querie) == len(word):
                # if 쿼리 매칭 확인 코드 작성 '?'나오면 스킵
                
                result += 1
            
        answer.append(result)
        
    # 이걸 어떻게 이진탐색으로 푸는거지?!...
        
    answer = []
    return answer