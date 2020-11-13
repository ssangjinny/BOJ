while(True):
    a = input()
    if a == '0' : break
    count = 0
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            count = count + 1

    if count > 0:
        print("no")
    elif count == 0:
        print("yes")
