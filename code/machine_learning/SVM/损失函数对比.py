import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    """不同的损失函数"""
    x = np.array(np.linspace(start=-3, stop=3, num=100, dtype=np.float))
    y_logit = np.log(1 + np.exp(-x)) / math.log(2)
    y_01 = x < 0
    y_hinge = 1.0 - x
    y_hinge[y_hinge < 0] = 0
    plt.plot(x, y_logit, 'r--', label='Logistic Loss', lw=2)
    plt.plot(x, y_01, 'g-', label='0/1 Loss', lw=2)
    plt.plot(x, y_hinge, 'b-', label='Hinge Loss', lw=2)
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()
