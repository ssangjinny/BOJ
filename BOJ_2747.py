N = int(input())
b = [0, 1]
for i in range(N):
    b.append(b[0+i]+b[1+i])

print(b[N])