a = int(input())
b = a
c = 0
if b < 10:
    b = (b * 10) + b
else:
    b = ((b % 10) * 10) + ((b % 10) + (b // 10))%10

c = c + 1
while a != b:
    if b < 10:
        b = (b * 10) + b
    else:
        b = ((b % 10) * 10) + ((b % 10) + (b // 10))%10

    c = c + 1
print(c)
