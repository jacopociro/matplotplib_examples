import numpy as np
import matplotlib.pyplot as plt
# how to plot 2d data on axes of 3d plot
ax = plt.figure().add_subplot(projection='3d')

# plot a sin  curve using x and y axes
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi)/2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# plot scatter data (20 2d point per colour)

colors = ('r', 'g', 'b', 'k')

np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list= []

for c in colors:
    c_list.extend([c]*20)

# zdir choose the axis that is fixed at 0
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')

# stuff
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20., azim=35, roll=0)

plt.show()