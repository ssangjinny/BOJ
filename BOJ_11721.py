c = 1
result = set(a for a in range(1, 10001))
l = set([])
for i in range(10000):
    if i < 10:
        c = i + i
        l.add(c)
    elif i < 100:
        c = i + (i//10) + (i%10)
        l.add(c)
    elif i < 1000:
        c = i + (i//100) + (i%10) + ((i%100 - i%10)//10)
        l.add(c)
    else:
        c = i + (i//1000) + (i%10) + ((i%100 - i%10)//10) + ((i%1000 - i%100)//100)
        l.add(c)
result = list(result - l)
result.sort()
for w in range(len(result)):
    print(result[w])