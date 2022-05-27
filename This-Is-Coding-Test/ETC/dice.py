def dice(casted):
    score = []
    passible = []
    temp = []
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    for x, y in casted:
        for i in range(x+y):
            temp.append([i, x+y-i])
        passible.append([temp])
        temp=[]
    
    # 레기드 배열 원소들이 만들 수 있는 모든 경우의 수를 map에 넣고 최적의 해를 추출
    map = []
    for list in passible:
        for x, y in list:
            pass
    return score


dice([[1,1],[5,6],[5,1],[5,5],[4,1],[6,6],[5,6],[5,6],[6,5],[3,6],[3,4]])
dice([[5,6],[4,6],[6,6],[6,3],[6,2],[2,5],[5,5],[6,5],[1,6],[2,4]])