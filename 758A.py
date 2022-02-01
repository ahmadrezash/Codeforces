if __name__ == "__main__":
	people_count = int(input())
	people_list = list(map(int, input().split()))
	max_welfare = max(people_list)

	need = []
	for person in people_list:
		need.append(max_welfare - person)

	print(sum(need))
