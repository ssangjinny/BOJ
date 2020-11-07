a = int(input())
i = 0
sum = 0
while (sum < a):
    i = i + 1
    sum = sum + i

x = sum - a
y = 1

if i % 2 == 0:
    for c in range(1, x + 1):
        y = y + 1
        i = i - 1

    print(str(i) + "/" + str(y))

else:
    for c in range(1, x + 1):
        y = y + 1
        i = i - 1

    print(str(y) + "/" + str(i))
