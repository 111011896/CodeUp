n = int(input())
dic = {}

def Fibonacci(n):
    if n in dic:
        return dic[n]
    if n == 1:
        dic[1] = 1
        return 1
    elif n == 2:
        dic[2] = 1
        return 1
    else:
        dic[n] = (Fibonacci(n-2) % 10009) + (Fibonacci(n-1) % 10009)
        return dic[n] % 10009

print(Fibonacci(n))
