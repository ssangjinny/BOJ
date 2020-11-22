A, B = map(int, input().split())
s1 = 0
s2 = 0
w1 = 0
w2 = 0
for i in range(1, A):
    s1 = s1 + i
    s2 = i*i

for w in range(1, B):
    w1 = w1 + w
    w2 = w*w

print(s1, s2, w1, w2)
