N = int(input())
a = N // 5
result = 0
count = [0, 0]
su = 0
bu = 0
if N % 5 == 0:
    result = N // 5
    print(result)
else:
    for i in range(N // 5, -1, -1):
        count[0] = i
        count[1] = 0
        su = i * 5
        while su < N:
            su = su + 3
            count[1] = count[1] + 1
        if su == N:
            bu = 1
            break
    result = sum(count)
    if bu == 0:
        result = -1
    print(result)
