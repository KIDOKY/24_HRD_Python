import matplotlib.pyplot as plt
import numpy as np

(fig, ax) = plt.subplots(nrows = 2, ncols = 2)
x = np.random.randn(100)
y = np.random.randn(100)
ax[0,0].scatter(x, y)
x = np.arange(10) # x축을 0 ~ 9
y = np.random.uniform(0, 10, 10)
ax[0, 1].bar(x, y)
y = np.eye(100)
ax[1, 1].imshow(y)
#plt.scatter(x, y)
plt.show()