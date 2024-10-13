#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(int, input().split()))
    A = int(input())
    B = int(input())
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a_max = a[0]
    i_max = 0
    for i, item in enumerate(a):
        if item >= a_max:
            i_max, a_max = i, item
    sum = 0
    for j in range(len(a)):
        if j > i_max:
            sum += a[j]

    s = 0
    for item in a:
        if A < item < B:
            s += 1

    b = sorted(a, key=abs, reverse = True)

    print(s)
    print(sum)
    print(b)
