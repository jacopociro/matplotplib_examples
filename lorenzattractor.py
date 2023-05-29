import numpy as np
import matplotlib.pyplot as plt

def lorenz(xyz, *, s=10,r=28, b=2.667):
    """
    Parameters
    ----------
    xyz: array-like, shpe(3,)
        Point of interest in 3D space
    s, r, b: float
        Parameters defining lorenz attractor.
    
    Returns
    -------
    xyz_dot : array, shape (3,)
        Values of the Lorenz attractor's partial derivatives at *xyz*
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    
    return np.array([x_dot, y_dot, z_dot])

dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., .105)

for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz attractor')

plt.show()