n = int(input())

def integer(n, start=1):
    if start > n:
        return
    print(start)
    start += 1
    integer(n, start)

integer(n)
