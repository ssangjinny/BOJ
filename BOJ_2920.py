a = list(map(int, input().split()))
b = [i for i in range(1, 9)]
c = [i for i in range(1, 9)]
c.reverse()
if a == b:
    print("ascending")
elif a == c:
    print("descending")
else :
    print("mixed")