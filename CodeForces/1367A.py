def calculate(word: str) -> str:
	decrypt: str = ""

	decrypt += word[0]
	for i in range(1, len(word), 2):
		decrypt += word[i:i + 1]
	return decrypt


if __name__ == '__main__':
	word_count = int(input())
	for i in range(word_count):
		word = input()
		print(calculate(word))
