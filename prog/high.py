#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from operator import indexOf
import math


# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = 4
    n = int(input())

    if n < 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    
    a = x
    k = 0
    Sum = a

    while math.fabs(x) > EPS:
        a *= ((x ** 2) / 4) / ((k + 1) * (k + 1 + n))
        Sum += a
        k += 1
    print(f"In{x} = {Sum * (x / 2) ** n}")
        