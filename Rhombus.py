def rhombus(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            if abs(j - (n-1)) <= (n-1 - abs(i - (n-1))):
                print("!", end = "")
            else:
                print(" ", end = "")
        print("")