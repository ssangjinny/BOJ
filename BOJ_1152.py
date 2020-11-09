a = input().split(" ")
if a[0] == "" and a[len(a) - 1] == "":
    print(len(a) - 2)

elif a[len(a) - 1] == "":
    print(len(a) - 1)

elif a[0] == "":
    print(len(a) - 1)

else:
    print(len(a))
