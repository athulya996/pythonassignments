# 6.Write a python program to print negative numbers in a list.
list = []
n = int(input("Enter the number of elements in list:"))
for i in range(0, n):
    ele = int(input("enter the element:"))
    list.append(ele)
print("The negative numbers in list are:", list)
for i in list:
    if i < 0:
        print(i, end=" ")