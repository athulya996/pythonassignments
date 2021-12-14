a = int(input("Enter the no. to be checked:"))
def power(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a,b//2) * power(a,b//2)
    return a * power(a, b // 2) * power(a,b//2)

def order(a):

    n = 0
    while (a != 0):
        n = n + 1
        a = a // 10
    return n

def is_Armstrong(a):
    n = order(a)
    temp = a
    sum = 0
    while (temp != 0 ):
         r = temp % 10
         sum = sum + power(r, n)
         temp = temp // 10
    return (sum == a)

print(is_Armstrong(a))
