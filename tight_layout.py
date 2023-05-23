import matplotlib.pyplot as plt
import numpy as np

## simple example
plt.rcParams['savefig.facecolor'] = "0.8"

def example_plot(ax, fontsize=12):
    ax.plot([1,2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)

plt.close('all')
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
# to avoid label going otuside of the figure
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# control the padding around the plot

# various format for which tight layout works
fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)

plt.tight_layout()

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1,0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1,2), rowspan=2)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()

# not tested but seems to work with subplots with aspcet not auto

arr = np.arange(100).reshape((10, 10))

fig = plt.figure(figsize=(5, 4))

ax = plt.subplot()
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()

# tightlayout considers all artists, extra space is indipendent of the original location of axes, pad=0 can clip text by few pixels

## use with grispec
import matplotlib.gridspec as gridspec

fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig, rect=[0, 0, 0.5, 1.0])
# rect specifies the bounding box where the subplot will be fit inside, it's complicated tho

## Legends and annotations

fig, ax = plt.subplots(figsize=(4, 3))
lines= ax.plot(range(10), label='A simple plot')
leg =ax.legend(bbox_to_anchor=(0.7, 0.5), loc='center left', )
# to have smaller fig not caring about label
leg.set_in_layout(False)
fig.tight_layout()

## Use with axesgrid1
from mpl_toolkits.axes_grid1 import Grid

plt.close('all')
fig = plt.figure()
grid = Grid(fig, rect=111, nrows_ncols=(2,2), axes_pad=0.25, label_mode='L')

for ax in grid:
    example_plot(ax)
ax.title.set_visible(False)
plt.tight_layout()

## colorbar
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")
plt.colorbar(im)
plt.tight_layout()

# you can also use axesgrid1
from mpl_toolkits.axes_grid1 import make_axes_locatable
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)
plt.tight_layout()

plt.show()
