a = list(input())
l = [str(c) for c in range(10)]
count = [0 for s in range(10)]
for i in range(len(a)):
    count[l.index(a[i])] += 1
if (count[6]+count[9])%2 == 0:
    count[6] = (count[6]+count[9])//2
    count[9] = count[6]
    print(max(count))
else :
    count[6] = (count[6] + count[9]) // 2 + 1
    count[9] = count[6]
    print(max(count))