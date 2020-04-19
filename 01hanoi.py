

def hanoi(n, a, b ,c, d):
    if n > 0:
        hanoi(n-1, a, c, b, 1)
        print('Moving from %s to %s  %s' % (a, c, d))
        hanoi(n-1 , b, a, c, 2)


hanoi(3, 'A', 'B', 'C', 0)