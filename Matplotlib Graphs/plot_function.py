import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**2

x = np.arange(-10, 10)

plt.plot(x, f(x))
plt.show()
