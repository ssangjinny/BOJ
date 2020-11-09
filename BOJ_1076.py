a = input()
b = input()
c = input()
dic = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey",
       "white")

for i in range(0, 10):
    if a == dic[i]:
        a = i

for i in range(0, 10):
    if b == dic[i]:
        b = i

for i in range(0, 10):
    if c == dic[i]:
        c = 10 ** i

print(((a*10)+b)*c)
