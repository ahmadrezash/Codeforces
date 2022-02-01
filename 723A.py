if __name__ == "__main__":
	distance_list = list(map(int, input().split()))
	print(max(distance_list)-min(distance_list))
