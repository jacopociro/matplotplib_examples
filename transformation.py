import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# data coordinates
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2) * np.sin(2*np.pi*x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

xdata, ydata = 5, 0

xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
bbox = dict(boxstyle="round", fc='0.8')
arrowprops = dict(arrowstyle='->', connectionstyle='angle, angleA=0, angleB=90, rad=10')

offset = 72
ax.annotate('data = (%.1f, %.1f)' %(xdata, ydata), (xdata, ydata), xytext=(-2*offset, offset), textcoords='offset points', bbox=bbox, arrowprops=arrowprops)

disp = ax.annotate('display = (%.1f, %.1f)' % (xdisplay, ydisplay),(xdisplay, ydisplay), xytext=(0.5*offset, -offset), xycoords='figure pixels', textcoords='offset points', bbox=bbox, arrowprops=arrowprops)

# Axes coordinates

fig = plt.figure()
for i, label in enumerate(('A', 'B', 'C', 'D')):
    ax = fig.add_subplot(2, 2, i+1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

fig, ax = plt.subplots()
x, y = 10*np.random.rand(2, 1000)
ax.plot(x, y, 'go', alpha=0.2)

circ = mpatches.Circle((0.5, 0.5), 0.25, transform=ax.transAxes, facecolor='blue', alpha=0.75)
ax.add_patch(circ)

# blended transformations
import matplotlib.transforms as transforms

fig, ax = plt.subplots()
x = np.random.randn(1000)

ax.hist(x, 30)
ax.set_title(r'$\sigma=1 \/ \dots \/ \sigma=2$', fontsize=16)

trans = transforms.blended_transform_factory( ax.transData, ax.transAxes)

rect = mpatches.Rectangle((1, 0), width=1, height=1, transform=trans, color='yellow', alpha=0.5)

ax.add_patch(rect)

# plotting in phyisical coordinates
fig, ax = plt.subplots(figsize=(7,2))
x,y = 10*np.random.rand(2, 1000)
ax.plot(x, y*10, 'go', alpha=0.2)
# circle in fixed coordinates
circ = mpatches.Circle((2.5, 2), 1.0, transform=fig.dpi_scale_trans, facecolor='blue', alpha=0.75)
# circle will be cropped
ax.add_patch(circ)

fig, ax = plt.subplots()
xdata, ydata = ((0.2, 0.7), (0.5, 0.5))
ax.plot(xdata, ydata, "o")
ax.set_xlim((0,1))

trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(xdata[0], ydata[0], ax.transData))

circle = mpatches.Ellipse((0, 0), 150/72, 130/72, angle=40, fill=None, transform=trans)

ax.add_patch(circle)

# using offset transforms to create a shadow effect
fig, ax = plt.subplots()

x = np.arange(0., 2., 0.01)
y = np.sin(2*np.pi*x)
line, = ax.plot(x, y, lw=3, color='blue')

dx, dy = 2/72., -2/72.
offset = transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)
shadow_transform = ax.transData + offset

ax.plot(x, y, lw=3, color='gray', transform=shadow_transform, zorder = 0.5*line.get_zorder())
ax.set_title('creating a shadow effect with an offest transform')

plt.show()