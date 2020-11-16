<<<<<<< HEAD
K, N = map(int, input().split())
l = []
s = 0
for _ in range(K):
    l.append(int(input()))
for i in range(1, sum(l)//N+1):
    j = 0
    for a in l:
        j = j + a//i
    if j == N:
        s = i
print(s)
=======
N, M = map(int, input().split())
l = []
for _ in range(N):
    l.append(int(input()))

>>>>>>> 2ce46b181571f5a323138baafbcd46a31e2eadee
