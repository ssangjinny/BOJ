N = int(input())
a = 0
b = 1
c = 0
for i in range(N):
    a = b
    b = c
    c = a + b

print(c)