case = int(input())

for g in range(0, case):
    size_x, size_y = map(int, input().split(' '))
    gold_mine = list(map(int, input().split(' ')))

    dp = []
    index = 0
    for i in range(size_x):
        dp.append(gold_mine[index:index + size_y])
        index += size_y

    for j in range(1, size_y):
        for i in range(size_x):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래서 오는 경우
            if i == size_x - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j + 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(size_x):
        result = max(result, dp[i][size_y - 1])
    
    print(result)