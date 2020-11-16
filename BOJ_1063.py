N = list(map(str, input().split()))
k_row = N[0][0]

steps = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
for i in range(int(N[2])):
