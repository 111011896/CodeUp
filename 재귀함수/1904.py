a, b = input().split()
a = int(a)
b = int(b)

def integer(a, b):
    if a > b:
        return
    if a % 2 == 0:
        a += 1
    else:
        print(a, end=' ')
        a += 2
    integer(a, b)

integer(a, b)
