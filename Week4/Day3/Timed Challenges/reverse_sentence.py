sentence = "You have entered a wrong domain"

text = sentence.split()

reverse_text = text[:: -1]

reverse_sentence = " ".join(reverse_text)

print(reverse_sentence)