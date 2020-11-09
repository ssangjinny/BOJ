a = int(input())
b = 3
if a % 2 == 0 :
    while b <= a//2:
        b = b + 1
        if a % b == 0:
            count = count + 1

else :
    b = 2
    while b <= a//2:
        b