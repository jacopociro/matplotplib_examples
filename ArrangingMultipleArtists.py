import matplotlib.pyplot as plt
import numpy as np

# basic 2x2 grid

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row},{col}]', (0.5,0.5), transform=axs[row,col].transAxes, ha='center', va='center', fontsize=18, color='darkgrey')

fig.suptitle('plt.subplots()')



# function
def annotate_axes(ax, text, fontsize=18):
    ax.text(0.5, 0.5, text, transform=ax.transAxes, ha="center", va="center", fontsize=fontsize, color="darkgrey")

# for subplot mosaic

fig, axd = plt.subplot_mosaic([['upper left', 'upper right',],[ 'lower left', 'lower right']], figsize=(5.5, 3.5), layout="constrained")
for k in axd:
    annotate_axes(axd[k], f'axd["{k}]', fontsize=14)
fig.suptitle('plt.subplot_mosaic()')

# grids of fixed-aspect ratio axes
fig, axs = plt.subplots(2, 2, layout="constrained", figsize=(5.5, 3.5))
for ax in axs.flat:
    ax.set_aspect(1)
fig.suptitle('Fixed aspect axes constrained')
# minimizes the space between grids
fig, axs = plt.subplots(2, 2, layout="compressed", figsize=(5.5, 3.5))
for ax in axs.flat:
    ax.set_aspect(1)
fig.suptitle('Fixed aspect axes compressed')

# Axes spanning rows or columns in a grid
fig, axd = plt.subplot_mosaic([['upper left', 'right'], ['lower left', 'right']], figsize=(5.5, 3.5), layout="constrained")

for k in axd:
    annotate_axes(axd[k], f'axd["{k}]', fontsize=14)
fig.suptitle('plt.subplot_mosaic()')

# variable width or height in a grid
gs_kw = dict(width_ratios=[1.4,1], height_ratios=[1,2])
fig, axd = plt.subplot_mosaic([['upper left', 'right'], ['lower left', 'right']], gridspec_kw=gs_kw, figsize=(5.5, 3.5), layout="constrained")
for k in axd:
    annotate_axes(axd[k], f'axd["{k}"]', fontsize=14)

fig.suptitle('plt.subplot_mosaic()')

# nested axes layout
fig = plt.figure(layout="constrained")
subfigs = fig.subfigures(1, 2, wspace=0.07, width_ratios=[1.5,1.])
axs0 = subfigs[0].subplots(2,2)
subfigs[0].set_facecolor('0.9')
subfigs[0].suptitle('subfigs[0]\nLeft side')
subfigs[0].supxlabel('xlabel for subfigs[0]')

axs1 = subfigs[1].subplots(3, 1)
subfigs[1].suptitle('subfigs[1]')
subfigs[1].supylabel('ylabel for subfigs[1]')

inner = [['innerA'], ['innerB']]
outer = [['upper left', inner], ['lower left', 'lower right']]

fig, axd = plt.subplot_mosaic(outer, layout="constrained")
for j in axd:
    annotate_axes(axd[j], f'axd["{j}"]')

## LOW-LEVEL AND ADVANCED GRID METHODS

# basic 2x2 grid 
fig = plt.figure(figsize=(5.5, 3.5), layout="constrained")
spec = fig.add_gridspec(ncols=2, nrows=2)

ax0 = fig.add_subplot(spec[0, 0])
annotate_axes(ax0, 'ax0')
ax1 = fig.add_subplot(spec[0, 1])
annotate_axes(ax1, 'ax1')
ax2 = fig.add_subplot(spec[1, 0])
annotate_axes(ax2, 'ax2')
ax3 = fig.add_subplot(spec[1, 1])
annotate_axes(ax3, 'ax3')

fig.suptitle('Manually added subplots using add_gridspec')

# axes spanning rows or grids in a grid
fig = plt.figure(figsize=(5.5, 3.5), layout="constrained")
spec = fig.add_gridspec(2,2)

# this is the same as [ax0, ax1], [ax1, ax2]
ax0 = fig.add_subplot(spec[0,:])
annotate_axes(ax0, 'ax0')

ax10 = fig.add_subplot(spec[1, 0])
annotate_axes(ax10, 'ax10')

ax11 = fig.add_subplot(spec[1, 1])
annotate_axes(ax11, 'ax11')

fig.suptitle('Manually added subplots, spanning a column')

# manual adjustment to gridspec layout
fig = plt.figure(layout=None, facecolor='0.9')
gs = fig.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.75, hspace=0.1, wspace=0.05)

ax0 = fig.add_subplot(gs[:-1,:])
annotate_axes(ax0, 'ax0')

ax1 = fig.add_subplot(gs[-1,:-1])
annotate_axes(ax1, 'ax1')

ax2 = fig.add_subplot(gs[-1,-1])
annotate_axes(ax2, 'ax2')

fig.suptitle('manual gridsce with right=0.75')

# more verbose version
fig =plt.figure(layout="constrained")
gs0 = fig.add_gridspec(1, 2)

gs00 = gs0[0].subgridspec(2, 2)
gs01 = gs0[1].subgridspec(3, 1)

for a in range(2):
    for b in range(2):
        ax = fig.add_subplot(gs00[a, b])
        annotate_axes(ax, f'axLeft[{a}, {b}]', fontsize=10)
        if a == 1 and b == 1:
            ax.set_xlabel('xlabel')
    for a in range(3):
        ax = fig.add_subplot(gs01[a])
        annotate_axes(ax, f'axRight[{a}, {b}]', fontsize=10)
        if a == 2:
            ax.set_xlabel('ylabel')

fig.suptitle('nested gridspec')

plt.show()