from itertools import permutations
N = int(input())
count = 0
l = []
for i in range(N):
    l.append(input())
K = int(input())
l = list(map(''.join, permutations(l)))
for a in range(len(l)):
    if int(l[a]) % K == 0:
        count += 1
print(count, len(l))
if len(l) % count == 0:
    print("1" + "/" + str(len(l) // count))
else:
    print(str(count) + "/" + str(len(l)))
