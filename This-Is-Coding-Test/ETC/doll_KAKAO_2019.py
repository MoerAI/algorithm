def solution(board, moves):
    n = len(board)
    box = []
    answer = 0    
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                pick_doll = board[i][m-1]
                board[i][m-1] = 0
                break
        else:
            pick_doll = 0
            
        if pick_doll != 0:
            box.append(pick_doll)

    for i in range(len(box)):
        index = 0
        temp = 0
        for e in box:
            if temp == box[index]:
                del box[index]
                del box[index-1]
                answer += 2
                break
            temp = box[index]
            index += 1
            if index >= len(box):
                break

    return answer

def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer