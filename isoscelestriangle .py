def triangle(n):
    space = 2 * n - 2
    for i in range(0, n):
        for j in range(0,space):
            print(end=" ")
        space = space - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n=5
triangle(n)


