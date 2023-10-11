#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = 0
    while a >= 0:
        if a == 7:
            break
        a += 1
        print("A")
    
    a = -1
    while a < 10:
        a += 1
        if a >= 7:
            continue
        print("A")
