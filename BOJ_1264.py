c = input()
l = ['a', 'e', 'i', 'o', 'u']
while c != '#':
    c = c.lower()
    count = 0
    for i in range(len(c)):
        if c[i] in l:
            count = count + 1
    print(count)
    c = input()