n = 9999999999

def isPrime(num):
	if num == 1:
		return False
	else:
		for i in range(2, int(num**0.5) + 1):
			if num % i == 0:
				return False
		return True

right_prime = []

for i in range(n+1):
  if(isPrime(i)):
    con = i
    while con > 10:
        con = int(con / 10)
        if (isPrime(con)):
            continue
        else:
            break
    if (isPrime(con)):
        right_prime.append(i)
        print(i)
print("END")

right_prime