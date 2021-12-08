print("Hi! Welcome to the love calculator :-) ")
name1 = input("Enter your name:")
name2 = input("Enter your partners name:")
c_names = name1 + name2
names = c_names
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
letters = t + r + u + e
l = names.count("l")
o = names.count("o")
v = names.count("V")
e = names.count("e")
letters1 = l + o + v + e

score = int(str(letters)+str(letters1))
if score <= 10 or score >= 80:
    print('your love score is',+score,'made for each other')
elif score >=40 or score <= 50:
    print('Your Love Score is',+score,'average couples')
else:
    print('Your Love Score is',+score,'poor couples')







