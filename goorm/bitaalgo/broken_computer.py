n, c = map(int, input().split(' '))
t = list(input().split(' '))
cnt, temp = 0, 0

for i in t:
	cnt += 1
	if int(i) - int(temp) > c:
		cnt = 1
	temp = i
print(cnt)