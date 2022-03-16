n = int(input())

def Factorial(n, initial=1):
    if n == 0:
        return print(initial)
    initial *= n
    n -= 1
    Factorial(n, initial)

Factorial(n)
