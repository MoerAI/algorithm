import sys
input = sys.stdin.readline

dics = {}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in dics:
        dics[tree] += 1
    else:
        dics[tree] = 1
    n += 1
        
tree_list = list(dics.keys())
tree_list.sort()
for tree in tree_list:
    print('%s %.4f' %(tree, dics[tree]/n*100))
