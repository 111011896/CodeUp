import sys
sys.setrecursionlimit(10**6)

n = int(input())

def Sum(n, sum=0):
    if n == 0:
        return print(sum)
    sum += n
    n -= 1
    Sum(n, sum)

Sum(n)
