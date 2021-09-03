i = 2;
sum = 1;

x = int(input("Enter a number: "))
while (i <= x//2 ):
    if (x % i == 0):    
        sum += i 
        i += 1  
		
    if sum == x: 
        print(x, "is a perfect number")
        break
    else:
        print(x, "is not a perfect number") 
        break

