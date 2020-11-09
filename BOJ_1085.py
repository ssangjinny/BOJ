import sys
arr = sys.stdin.readline().restrip()
a = arr[0] - arr[1]
b = arr[2] - arr[3]
c = [abs(a), abs(b)]
c.sort()
print(c[0])