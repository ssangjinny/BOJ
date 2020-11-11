c = input().upper()
a = []
for x in set(c):
    a.append(c.count(x))
ma = [x for x, i in enumerate(a) if i == max(a)]
if len(ma) > 1:
    print("?")
else:
    print(list(set(c))[a.index(max(a))])
