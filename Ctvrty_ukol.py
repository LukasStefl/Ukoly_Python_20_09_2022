n = int(input("Enter the range: \t "))
for rows in range(n, 0, -1):
    for columns in range(0, rows):
        print("*", end=" ")
    print()