N = int(input())
count = 0
while True:
    if N == 1:
        break
    elif N % 3 == 0:
        N = N // 3
        count += 1
    elif (N - 1) % 3 == 0:
        N = N - 1
        count += 1
    elif N % 2 == 0:
        N = N // 2
        count += 1
    elif (N - 1) % 2 == 0:
        N = N - 1
        count += 1
    else:
        N = N - 1
        count += 1

print(count)
