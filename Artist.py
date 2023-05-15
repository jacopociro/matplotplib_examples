import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib as mpl
import numpy as np


fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax = fig.add_subplot(2, 1, 1)

ax.set_ylabel('Voltage [v]')
ax.set_title('A sine wave')

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)
n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor='yellow', edgecolor='yellow')

ax2.set_xlabel('Time [s]')

# figure container
fig2 = plt.figure()
l1 = lines.Line2D([0, 1], [0, 1], transform=fig2.transFigure, figure=fig2)
l2 = lines.Line2D([0, 1], [1, 0], transform=fig2.transFigure, figure=fig2)
fig2.lines.extend([l1,l2])

# axes container
fig3 = plt.figure()

ax3 = fig3.add_subplot(111)
rect = ax3.patch
rect.set_facecolor('green')
x, y = np.random.rand(2,100)
line, = ax3.plot(x, y, '-', color='blue', linewidth=2)
ax4 =fig3.add_subplot(222)
n, bins, rectangles = ax4.hist(np.random.randn(1000), 50)

fig4, ax4 = plt.subplots()

rect2 = mpl.patches.Rectangle((1, 1), width=5, height=12)

ax4.add_patch(rect2)
ax4.autoscale_view()

fig.canvas.draw()

# axis container
fig5 = plt.figure()
rect3 = fig.patch
rect3.set_facecolor('lightgoldenrodyellow')

ax5 = fig5.add_axes([0.1, 0.3, 0.4, 0.4])
rect3 = ax5.patches
rect.set_facecolor('lightslategray')

for label in ax5.xaxis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(45)
    label.set_fontsize(16)

for line in ax5.yaxis.get_ticklines():
    line.set_color('green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)

# tick containers

np.random.seed(19680801)

fig6, ax6 = plt.subplots()
ax6.plot(100*np.random.rand(20))

ax6.yaxis.set_major_formatter('${x:1.2f}')

ax6.yaxis.set_tick_params(which='major', labelcolor='green', labelleft=False, labelright=True)
plt.show()