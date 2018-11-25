def maketriangle(x):
    for i in range(1,x+1):
        for j in range(0,i):
            print("#",end="")
        print("\r")

x=5
maketriangle(x)