C = int(input())
for i in range(C):
    count = 0
    l = list(map(int, input().split()))
    a = (sum(l) - l[0])/l[0]
    for w in range(1, len(l)):
        if a < l[w]:
            count += 1
    b = "%0.3f" % (count/l[0]*100)
    print(str(b) + "%")
