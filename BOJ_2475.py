a = list(map(int, input().split()))
for x in range(len(a)):
    a[x] = a[x] ** 2

b = sum(a)%10
print(b)