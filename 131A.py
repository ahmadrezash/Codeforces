from typing import List


def is_wrong(word:str):
	# only contains uppercase letters
	letter_status = list(map(lambda l: l.isupper(), word))
	condition1 = all(letter_status)

	# all letters except for the first one are uppercase
	letter_status = list(map(lambda l: l.isupper(), word[1:]))
	condition2 = all(letter_status) and word[0].islower()

	return condition1 or condition2


if __name__ == '__main__':
	word: str = input()
	if is_wrong(word):
		letter_list = list(map(lambda l: l.lower() if l.isupper() else l.upper(), word))
		word = "".join(letter_list)
	print(word)
