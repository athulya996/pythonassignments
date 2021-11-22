
# 2. Python program to find the smallest number in a list.
list = []
n = int(input("Enter the number of elemnts in a list:"))
for i in range(1, n+1):
    ele = input("Enter the number:")
    list.append(ele)
print("your current list is :", list)
print("smallest no is:", min(list))

