# 3.Write a python program to print even numbers in a list.
def even(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

list = []
n = int(input("Enter the number of elements in list:"))
for i in range(0, n):
    ele = int(input("enter the element:"))
    list.append(ele)
print("Even numbers in list are:", list)
print(even(list))


