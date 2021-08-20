import math, time

def convert_10_any(n, b):
    x = ""
    r = n
    c = 0
    while r >= 1:
        x = str(r % b) + x
        r = r // b
        c += 1
    print(f"{c} iterations")
    return x

def convert_any_10(n, b):
    n = str(n)
    r = 0
    for i in range(0, len(n)):
        r += int(n[(-i-1)]) * b ** i
    return r


def convert_any_any(n, a, b):
    dec = convert_any_10(n, a)
    result = convert_10_any(dec, b)
    return result

def timer(f, *args):
    t0 = time.time()
    r = f(args)
    t1 = time.time()
    print(f"{r}\t | {t1-t0} ms")