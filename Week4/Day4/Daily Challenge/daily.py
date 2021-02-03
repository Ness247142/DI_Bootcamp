# import re

# x,y = list(map(int,input().split()))

# rows =[input() for i in range(x)]

# text = "".join([row[i] for i in range(y) for row in rows])

# text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)

# text = re.sub('  ', ' ', text)

# print(text)


text = " "

matrix = [
    ["7","i","3"],
    ["T", "s", "i"],
    ["h", "%" ,"x"],
    ["i"," ","#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    [" ", "r", "!"]
]

for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        if matrix[y][x].isalpha() or matrix[y][x] == " ":
            text += matrix[y][x]

print(text)
print(len(text))