#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from operator import indexOf
import math


EPS = 1e-10

if __name__ == '__main__':
    x = float(input())
    n = int(input())

    if n < 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    
    if x == 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    
    a = x
    S, k = a, 1

    while math.fabs(a) > EPS:
        a *= ((x ** 2) / (4 * (k ** 2) + 4 * k * n + 8 * k + 4 * n + 4))
        S += a
        k += 1
    
    print(f"I({n})({x}) = {S * (x / 2) ** n}")
        