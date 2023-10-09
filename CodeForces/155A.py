from typing import List


def calculate(score_list: List[int]) -> int:
	min_score = score_list[0]
	max_score = score_list[0]

	amazing_performance = 0

	for score in score_list:
		if score < min_score:
			min_score = score
			amazing_performance += 1
		if score > max_score:
			max_score = score
			amazing_performance += 1
	return amazing_performance


if __name__ == "__main__":
	contest_count = int(input())
	str_list = input()
	score_list = list(map(int, str_list.split()))
	print(calculate(score_list))
