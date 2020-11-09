a = input()
a = a.upper().solt().split()
x = 0
y = 1
for x in a:
    if a[x] == a[x + 1]:
        y = y + 1
        if count < y :
            count = y

    else:
        count = y
        y = 1
