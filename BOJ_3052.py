d = []
for _ in range(10):
    N = int(input())
    d.append(N % 42)
print(len(set(d)))