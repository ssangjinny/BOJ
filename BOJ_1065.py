N = int(input())
count = 0
a = 0
b = 0
c = 0
for i in range(1, N+1):
    if 1 <= i <= 99:
        count += 1
    else:
        a = (i - (i%100))//100
        b = (i - (i - (i%100)) - (i%10))//10
        c = i%10
        if (a-b) == (b-c):
            count += 1
print(count)