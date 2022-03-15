a, b = input().split()
a = int(a)
b = int(b)

def PrintOddNumber(a, b):
    if a > b:
        return
    if a % 2 == 0:
        a += 1
    else:
        print(a, end=' ')
        a += 2
    PrintOddNumber(a, b)

PrintOddNumber(a, b)
