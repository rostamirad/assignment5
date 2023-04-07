def Khayyam_Pascal(n):
    Array = []
    for i in range(n):
        Array.append([0]*(i+2))
        Array[i][0] = 1
        print(Array[i][0], end = "  ")

        for j in range(1, i+1):
            Array[i][j] = Array [i-1][j-1] + Array[i-1][j]
            print(Array[i][j], end = "  ")
        print("")