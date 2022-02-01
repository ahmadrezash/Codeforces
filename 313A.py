def calculate(number: int):
	x1 = int(str(number)[:-1])
	x2 = int(str(number)[:-2] + str(number)[-1])

	return max(x1, x2, number)


if __name__ == '__main__':
	n = int(input())
	print(calculate(n))
