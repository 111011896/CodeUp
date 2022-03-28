n = int(input())

def HailstoneNum(n):
    print(n)
    if n == 1:
        return
    if n % 2 != 0:
        n = int(3*n+1)
        return HailstoneNum(n)
    else:
        n = int(n/2)
        return HailstoneNum(n)

HailstoneNum(n)
