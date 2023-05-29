import numpy as np
import matplotlib.pyplot as plt

# create 2d bar graphs in different planes

np.random.seed(19680801)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y']

yticks = [3, 2, 1, 0]

for c, k in zip(colors, yticks):
    # random data
    xs = np.arange(20)
    ys = np.random.rand(20)

    # first bar of each set is cyan
    cs = [c] * len(xs)
    cs[0] = 'c'

    ax.bar(xs, ys, zs = k, zdir='y', color=cs, alpha = 0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_yticks(yticks)

plt.show()