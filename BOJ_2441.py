A = int(input())
for i in range(A, 0, -1):
    for a in range(A-i):
        print(" ", end="")
    print("*"*i)