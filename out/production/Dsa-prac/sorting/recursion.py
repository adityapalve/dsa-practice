def recurse(n):
    if n == 1:
        print(1)
        return print("End")

    recurse(n-1)
    print(n)
    print("end")


recurse(5)


