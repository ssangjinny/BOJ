c = input()
for _ in range(int(c)):
    a, b = map(str, input().split())
    c = []
    for x in range(len(b)):
        c.append(b[x]*int(a))

    c.append('\n')
    for x in range(len(c)):
        print(c[x], end="")