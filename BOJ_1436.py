N = int(input())
count = 0

for i in range(666, 10000000):
    if '666' in str(i):
        count = count + 1
        if N == count:
            break
print(i)