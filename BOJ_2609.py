N = list(map(int, input().split()))
mod = max(N) % min(N)
a = max(N)
b = min(N)
while(mod > 0):
    a = b
    b = mod
    mod = a % b
print(b)
print(max(N)*min(N)//b)