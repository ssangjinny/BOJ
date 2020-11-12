N = int(input())
a = list(map(int, input().split()))
b = max(a)
for i in range(len(a)):
    a[i] = a[i]/b*100

print(sum(a)/len(a))