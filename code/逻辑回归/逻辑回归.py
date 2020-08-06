import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)
x = np.linspace(-7, 7, 101)
y = 1 / (1 + np.exp(-x))

plt.figure(figsize=(6, 4))
plt.plot(x, y, 'r-', lw=3)
plt.show()
