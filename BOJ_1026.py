N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B, reverse=True)
su = 0
for i in range(N):
    su = su + A[i]*B[i]
print(su)