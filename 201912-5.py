# -*- coding: utf-8 -*-
from sys import stdin

def f(x):
    return (x % 2009731336725594113) % 2019


def run():
    u0 = 314882150829468584
    u1 = 427197303358170108
    u2 = 1022292690726729920
    u3 = 1698479428772363217
    u4 = 2006101093849356424

    uu = [u0, u1, u2, u3, u4]

    n, q = map(int, input().split())
    aa = [i for i in range(n + 1)]

    for line in stdin:
        l, r = map(int, line.split())
        sum = 0
        for i in range(l, r + 1):
            sum += (aa[i] % 2009731336725594113) % 2019

        print(sum)

        t = sum % 5
        ut = uu[t]
        for i in range(l, r + 1):
            aa[i] = aa[i] * ut % 2009731336725594113


if __name__ == "__main__":
    run()