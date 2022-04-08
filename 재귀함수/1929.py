n = int(input())
lst = []

def HailstoneNum(n):
    lst.append(n)
    if n == 1:
        return
    if n % 2 != 0:
        n = int(3*n+1)
        return HailstoneNum(n)
    else:
        n = int(n/2)
        return HailstoneNum(n)

HailstoneNum(n)
lenth = len(lst)

def ReverseNum(lenth):
    if lenth == 0:
        return
    else:
        print(lst[lenth-1])
        lenth -= 1
        return ReverseNum(lenth)

ReverseNum(lenth)
