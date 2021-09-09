
# Take the following inputs 5 times from the user:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple will contain a name, age and score
# Sort the list by the following priority Name > Age > Score

def info():
    unordered_list = []
    sorted_list = []
    for _ in range(5):
        info = []
        info.append(str(input("Name: ")))
        info.append(int(input("Age: ")))
        info.append(int(input("Score: ")))
        unordered_list = tuple(info)
        sorted_list.append(unordered_list)
        
    sorted_list.sort(key=lambda  x:(x[0], x[1], x[2]))
    print(sorted_list)

print(info())
