l = list(input())
c = []
for i in range(len(l)):
    for a in range(1, len(l)):
        c.append(l[0:i:-1] + l[i:a:-1] + l[a:len(l) - 1:-1])

print(c)
