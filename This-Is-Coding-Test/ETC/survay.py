def error(replies, n, k):
    temp =[]
    for replie in replies:
        temp.append(0)
        for i in range(len(replie)):
            temp.append(replie[i:i+n])

    check_point = ""
    for ans in temp:
        if ans == 0:
            check_point = ""
        


replies = ["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFF", "FCBBBFCBBECBB"]
n = 3
k = 2
error(replies, n, k)
