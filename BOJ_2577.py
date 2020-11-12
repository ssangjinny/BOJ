a = int(input())
b = int(input())
c = int(input())
d = list(str(a*b*c))
e = [str(i) for i in range(0, 10)]
for x in e:
    count = 0
    for y in d:
        if x == y:
            count = count + 1
    print(count)