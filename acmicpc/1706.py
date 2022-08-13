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