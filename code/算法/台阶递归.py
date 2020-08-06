# 递归法
def getNum1(num):
    assert num >= 0, "num > 0"
    if num <= 1:
        return 1
    else:
        return getNum1(num - 1) + getNum1(num - 2)


# 非递归（减而治之）
def getNum2(num):
    a, b = 1, 1
    while num > 1:
        a, b = b, a + b
        num -= 1
    return b


# 动态规划
def getNum3(num):
    a, b = 1, 1
    for _ in range(num):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    # 递归法
    num1 = getNum1(20)
    print(num1)

    # 线性非递归
    num2 = getNum2(20)
    print(num2)

    # 动态规划
    num3 = getNum3(20)
    print(num3)
