# n = int(input("Enter your limit :"))
# def pattern(n):
#     for i in range(n,1,-1):
#         for j in range(0,i-1):
#             print("*",end=" ")
#         print("\r")
# pattern(n)


rows = int(input("Enter number of rows: "))

a = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while a != (2 * i - 1):
        print("* ", end="")
        a += 1

    a = 0
    print()