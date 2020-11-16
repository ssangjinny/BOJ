N = int(input())
l = []
for i in range(N):
    l.append(list(input()))
for a in range(len(l[0])):
    for b in range(1, N):
        if l[b-1][a] != l[b][a]:
            l[0][a] = "?"

print("".join(l[0]))