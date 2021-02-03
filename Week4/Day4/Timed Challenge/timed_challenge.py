def occurrence(ch, str1):
    count = 0
    for i in range(len(string)):
        if(string[i] == char):
            count = count + 1
    return count

string = input("Enter your text: ")
char = input("Enter your character: ")

last_count = occurrence(char, string)
print(char, " has occurred ", last_count, "time(s)")