def multiplication_table(n, m):
    for i in range(1, n):
        for j in range(1,m):
            print(i*j, end = "  ")
        print("")