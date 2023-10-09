from typing import List


def calculate(a: List[int]) -> int:
	agent_count = 0
	crime_count = 0
	for i in a:
		if i >= 1:
			agent_count += i
		elif i == -1:
			if agent_count > 0:
				agent_count -= 1
			else:
				crime_count += 1
	return crime_count


if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	print(calculate(a))
