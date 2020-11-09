a = int(input())
l = []
for b in range(0, a):
    l.append(int(input()))

l.sort()
for b in range(0, a):
    print(str(l[b]))