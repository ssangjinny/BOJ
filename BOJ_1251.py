l = input()
c = []
a = 0
w = ""
for i in range(1, len(l)-1):
    w1 = l[0:i]
    a = a + 1
    for a in range(i+1, len(l)):
        w2 = l[i:a]
        w3 = l[a:len(l)]
        c.append([w1[::-1], w2[::-1], w3[::-1]])

for q in range(len(c)):
    c[q] = "".join(c[q])

c = sorted(c, key=str.lower)
print(c[0])