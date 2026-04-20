# Session 5 - ASTR 19 Code Journal

import math

def main():
    n = 1000
    start = 0
    end = 2 * math.pi
    step = (end - start) / n

    x = start
    for i in range(n):
        print(x, math.sin(x))
        x += step


if __name__ == "__main__":
    main()