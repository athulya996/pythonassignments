#1. Python program to interchange first and last elements in a list
list = []
n = int(input("Enter the number of elements in a list:"))
for i in range(0, n):
    ele = input("Enter the element:")
    list.append(ele)

print("your current list is :", list)
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print("your new list is:", list)


