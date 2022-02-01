def calculate(a: int, b: int) -> int:
	dist: int = abs(a - b)
	step_count: int = 0

	step_count += dist // 10

	if dist % 10 != 0:
		step_count += 1

	return step_count


if __name__ == '__main__':
	n: int = int(input())
	for i in range(n):
		a, b = map(int, input().split())
		print(calculate(a, b))
