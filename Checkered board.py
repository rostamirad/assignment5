# n is row and m is column:)
def Checkered_board(n : int , m : int):
    for i in range(n):
        for j in range(m):
            if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
                print("#", end = "")
            else:
                print("*", end = "")
        print("")