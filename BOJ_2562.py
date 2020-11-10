a = [int(input()) for _ in range(9)]
b = 0
c = a[0]
for i in range(8):
    if c < a[i + 1]:
        c = a[i + 1]
        b = i + 1

print(a[b])
print(a.index(a[b]) + 1)