test = int(input())
for _ in range(test):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    re = l[M]
    count = 0
    bu = 0
    for a in l:
        for i in range(len(l)):
            if l[i] == max(l):
                l[i] = 0
                count = count + 1
                if l[M] != re:
                    bu = 1
                    break
        if bu == 1:
            bu = 0
            break
    print(count)

