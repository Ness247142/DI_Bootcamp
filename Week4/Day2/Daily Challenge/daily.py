birthday = input("Input your birthdate. Write it DD/MM/YYYY: ")
candle_number = int(birthday[-1])
day, month, year = birthday.split(' ')
day = int(day)
month = int(month)
year = int(year)
top_cake = int((11-candle_number)/2)  

space = " "
roof = "^"
line = "_"
candle = "i"
bottom = "~"


def birthday_cake():
    print(f"{4*space}{top_cake*line}{candle_number*candle}")
    print(f"{3*space}|:H :a :p :p :y :|")
    print(f"{1*space}{2*line}|{11*line}|{2*line}")
    print(f"|{17*roof}|")
    print(f"|:B :i :r :t :h :d :a :y :|")
    print(f"|{17*space}|")
    print(f"{19*bottom}")
    
    if year == 0:
        cake()
        print("")
        cake()
    else:
        cake()
