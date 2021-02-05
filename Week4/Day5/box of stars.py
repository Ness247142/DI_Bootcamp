def get_longest_word_length(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


def draw_starline(length):
    print("*"*(length + 4))


def draw_wordlines(words, longest):
    for word in words:
        spaces = " "*(longest - len(word))
        print(f"* {word}{spaces} *")


def run():
    text = input("Enter a sentence: ")
    text_list = text.split(" ")
    longest = get_longest_word_length(text_list)
    draw_starline(longest)
    draw_wordlines(text_list, longest)
    draw_starline(longest)


run()
