n = int(input("Enter the number: "))

for i in range (1, n):
    factors = 1

    for j in range (2, i+1):
        if i%j == 0:
            factors += 1 

    if factors == 2:
        print(f"{i} is a prime number")
 