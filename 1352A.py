def factor(n):
	count = 0
	fact = []
	str_n = str(n)
	for i in range(0, len(str_n)):
		if str_n[i] != '0':
			fact.append(int(str_n[i]) * (10 ** (len(str_n) - i - 1)))
			count += 1
	print(count)
	print(" ".join(str(x) for x in fact))


if __name__ == '__main__':
	k = int(input())

	for i in range(0, k):
		n = int(input())
		factor(n)
