r, c = map(int, input().split())
cross = []
result = []
for _ in range(r):
    s = input()
    cross.append(s)

for s in cross:
    result.extend(s.split('#'))

for i in range(c):
    word = ''
    for j in range(r):
        word += cross[j][i]
    result.extend(word.split('#'))

result = list(filter(lambda x: len(x) > 1, result))
print(sorted(result)[0])

    # for i in range(c):
    #     if s[i] != '#':
    #         word += s[i]
    #     elif (s[i] == '#') & (len(word) >= 2):
    #         dic.add(word)
    #         word = ''
    #         if len(s[i:]) == 1:
    #             break
    # if s not in '#':
    #     dic.add(word)
    #     word = ''
    
print(dic)