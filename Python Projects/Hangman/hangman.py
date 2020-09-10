# Write your code here
import random

def menu():
	opt = input('Type "play" to play the game, "exit" to quit: ')


def check_letter(letter):
	global count
	if len(letter) != 1:
		print("You should input a single letter")
		return False
	if letter.isupper() or not letter.isalpha():
		print("It is not an ASCII lowercase letter")
		return False
	if letter in used_set:
		print("You already typed this letter")
		return True
	elif letter in letter_set:
		used_set.add(letter)
		return True
	else:
		used_set.add(letter)
		count += 1
		return False
	

def reveal_letter(letter):
	for i in range(len(correct_ans)):
		if letter == correct_ans[i]:
			censor_word[i] = letter
	return "".join(censor_word)


print("H A N G M A N\n")
while True:
	option = input('Type "play" to play the game, "exit" to quit: ')
	if option == "play":
		# Shuffle words in list and select the first word in the list
		word_list = ['python', 'java', 'kotlin', 'javascript']
		random.shuffle(word_list)
		correct_ans = word_list[0]
		current_ans = ""
		count = 0

		# Breaks selected word into letters in a set
		letter_set = set(correct_ans)
		used_set = set()

		censor_word = list()
		for i in range(0, len(correct_ans)):
		    censor_word += "-"
		current_ans = "".join(censor_word)
		print(current_ans)

		while count < 8:
			user_input = input("Input a letter: ")
			checker = check_letter(user_input)
			if checker:
				current_ans = reveal_letter(user_input)
			else:
				print("No such letter in the word")

			if current_ans == correct_ans:
				break
			if count == 8: break
			print("\n" + current_ans)

		if current_ans == correct_ans:
			print("You guessed the word!\nYou survived!")
		else:
			print("You are hanged!")
	elif option == "exit":
		break
