N = int(input())
F = int(input())
N = N - N % 100
while N % F != 0:
    N = N + 1

N = N % 100
if N < 10:
    N = str(N)
    N = str(0) + N

print(N)
