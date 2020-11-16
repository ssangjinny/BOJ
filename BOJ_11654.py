N = int(input())
for _ in range(N):
    a = input()
    score = 0
    count = 0
    for i in range(len(a)):
        if a[i] == 'O':
            count = count + 1
            score = score + count
        else :
            count = 0
    print(score)