# Variables for the program
possible_words = []
letter = 'a'
position = 1
word_list = []

print("Wordle Helper By Parth Bhangla \n")
print("This program uses basic elimination on all the acceptable answers of wordle to solve it.")
print("To use this, you need to make the first guess and then feed the information you get into to program and take another guess from the remaining words list and continue doing so until you find the answer. \n")

try:
    with open("answers.txt", "r") as f:
        possible_words = f.readlines()
except FileNotFoundError:
    print("Error: 'answers.txt' not found.")
    exit()

while letter != '':

    word_list.clear()

    letter = input("What letter do you know? ")
    colour = input("What colour is the letter (b, y, g)? ")

    if colour == 'g' or colour == 'y':
        position = int(input("What position is the letter in (1-5)? ")) - 1
    
    for word in possible_words:
        if colour == 'g' and word[position] == letter:
             word_list.append(word)

        elif colour == 'y' and letter in word and word[position] != letter:
            word_list.append(word)

        elif colour == 'b' and letter not in word:
                word_list.append(word)

    possible_words = word_list.copy()
    print("Remaining Possible Words: \n")
    print(*word_list, end='\n')
        