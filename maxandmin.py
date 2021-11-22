t = tuple()
n = int(input("Total number of values in tuple :"))
for i in range (n):
    a = input("Enter the elements:")
    t = t+(a,)
print("maximum value =",max(t))
print("minumum value =",min(t))