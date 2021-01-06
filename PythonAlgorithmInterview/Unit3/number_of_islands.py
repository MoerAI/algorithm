# leetcode 200 : Number of Islands
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.
# (연결되어 있는 1의 덩어리 개수를 구하라.)
# input1  : 11110
#           11010
#           11000
#           00000
# output1 : 1
# input2  : 11000
#           11000
#           00100
#           00011
# output1 : 1

# DFS로 그래프 탐색
def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(i, j):
    # 더 이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid) or \
        grid[i][j] !='1':
            return
        
    grid[i][j] = 0
    
    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count