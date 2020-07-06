import math
import numpy as np
from time import time


def is_prime(x):
    return 0 not in [x % i for i in range(2, int(math.sqrt(x)) + 1)]


def is_prime2(x):
    flag = True
    p_list = []
    for p in p_list:
        if p > math.sqrt(x):
            break
        if x % p == 0:
            flag = False
    if flag:
        p_list.append(x)
    return p_list


if __name__ == '__main__':
    a = 2
    b = 1000000

    # 方法1：直接计算
    t = time()
    p = [p for p in range(a, b) if 0 not in [p % d for d in range(2, int(math.sqrt(p)) + 1)]]
    print(time() - t)
    print(p)

    # 方法2：使用filter
    t = time()
    p = list(filter(is_prime, list(range(a, b))))
    print(time() - t)
    print(p)

    # 方法3：使用filter和lambda
    t = time()
    is_prime2 = (lambda x: 0 not in [x % i for i in range(2, int(math.sqrt(x)) + 1)])
    p = list(filter(is_prime2, list(range(a, b))))
    print(time() - t)
    print(p)

    # 方法4：定义
    t = time()
    p_list = []
    for i in range(2, b):
        flag = True
        for p in p_list:
            if p > math.sqrt(i):
                break
            if i % p == 0:
                flag = False
                break
        if flag:
            p_list.append(i)
    print(time() - t)
    print(p)
