# 고속거듭제곱 알고리즘
#  def power(a,b,m):
# 	result = 1
# 	while b > 0:
# 		if b % 2 != 0:
# 			result = (result * a) % m
# 		b //= 2
# 		a = (a * a) % m

# 	return result

n = int(input())
answer = 0
for i in range(1, n+1):
	answer = answer + i*i*i

print(answer%1000000007)