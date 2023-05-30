from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# animation
import time
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xs = np.linspace(- 1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)

ax.set_zlim(-1, 1)

# begin plotting
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    # plot new wireframe
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)

print('Average FPS: %f' % (100 / (time.time() - tstart)))

# wireframe in one direction

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})

X, Y, Z = axes3d.get_test_data(0.05)

ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title('Column (x) stride set to 0')

ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title('Row (y) stride set to 0')

plt.tight_layout()
plt.show()