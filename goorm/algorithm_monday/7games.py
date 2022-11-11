for _ in range(5):
	user_input = list(str(input()))
	a = int(user_input[0]) + int(user_input[2]) + int(user_input[4]) + int(user_input[6])
	if int(user_input[1]) != 0:
		a = a * int(user_input[1])
	if int(user_input[3]) != 0:
		a = a * int(user_input[3])
	if int(user_input[5]) != 0:
		a = a * int(user_input[5])
	print(a%10)