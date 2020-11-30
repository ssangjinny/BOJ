import sys
N = int(sys.stdin.readline().rstrip())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline().rstrip()))
l.sort()
for a in range(len(l)):
    print(l[a])