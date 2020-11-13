a = int(input())
b = []
for _ in range(a):
    b.append(input())

b = sorted(set(b), key=lambda x: (len(x), x))
for i in b:
    print(i)
