a: list
a = list(map(lambda x: x + 10, [1,2,3]))
print(a)
b: list
b = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(b)
print(type(b))