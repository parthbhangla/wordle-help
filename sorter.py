input = open('words.txt', 'r')
output = open('five_letter_words.txt', 'w')
for word in input:
    word = word.strip().lower()
    if len(word) == 5 and word.isalpha():
        output.write(word+"\n")
    else:
        continue
input.close()
output.close()