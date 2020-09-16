from itertools import chain
# 지운이형이 써준거
#def solution(n, directory, query):
#    path = defaultdict(list)
#    for b, e in directory:
#        path[b].append(e)

#    for b, e in query:
#        now = set([b])
#        visited = [False] * n
#        while True:
#            for b in now:
#                visited[b] = True
#            if visited[e]:
#                break
#            now = set(filter(lambda x: not visited[x], chain(*(path[b] for b ))))
            
def solution(n, directory, query):
    answer = []   
    path = {i: [] for i in range(n+1)}
    for folder, node in directory:
        path[folder].append(node)
        path[node].append(folder)
    print(path)
    for start, end in query:
        print(start, end, 'wtf')
        now = set([start])
        visited = [False] * (n + 1)
        result = 0
        while True:
            for start in now:
                visited[start] = True
            if visited[end]:
                break
            print (now, visited)
            now = set(filter(lambda x: not visited[x], chain(*(path[start] for start in now))))
            print('next', now)
            result += 1
        answer.append(result + 1)
    return answer
    
print(solution(5,[[1,2],[1,3],[2,4],[2,5]],[[1,5],[2,5],[3,5],[4,5]]))