import numpy as np

import matplotlib.pyplot as plt


# 添加主题样式


# 设置图的大小，添加子图

fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(111)


for color in ['red', 'green','blue','yellow']:

    n = 10

    x, y = np.random.rand(2, n)

    scale = 100.0 * np.random.rand(n)

    ax.scatter(x, y, c=color, s=scale,

                label=color, alpha=0.5,

                edgecolors='none',edgecolor=color)

ax.legend()

ax.grid(True)
ax.legend(loc='lower right')
plt.show()

