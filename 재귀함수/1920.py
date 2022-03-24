import math

n = int(input())

def Binary(n, initial='', devide=0):
    if initial == '' and n == 0:
        return '0'
    if initial == '':
        index = math.trunc(math.log2(n))
        devide = 2 ** index
        share = n // devide
        remainder = n % devide
    else:
        share = n // devide
        remainder = n % devide
    if devide < 1:
        return initial
    if share == 1:
        n = remainder
        devide = devide / 2
        initial += '1'
        return Binary(n, initial, devide)
    elif share == 0:
        devide = devide / 2
        initial += '0'
        return Binary(n, initial, devide)

print(Binary(n))
