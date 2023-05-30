import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

def randrange(n, vmin, vmax):
    """
    helper function to make an array of random numbers having shape (n, ) with each number distributed uniform(vmin, vmax)
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n , 23, 32)
    ys = randrange(n, 0 , 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

plt.show()