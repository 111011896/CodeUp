n = int(input())

def integer(n):
    if n == 0:
        return
    print(n)
    n -= 1
    integer(n)

integer(n)
