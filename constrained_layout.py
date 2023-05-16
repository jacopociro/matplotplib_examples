import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 4.5, 4.
plt.rcParams['figure.max_open_warning'] = 50

def example_plot(ax, fontsize=12, hide_labels=False):
    ax.plot([1, 2])
    ax.locator_params(nbins=3)
    if hide_labels:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    else:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)

fig, ax = plt.subplots(layout="constrained")
example_plot(ax, fontsize=24)

# multiple subplots
fig, axs = plt.subplots(2, 2, layout="constrained")

for ax in axs.flat:
    example_plot(ax)

# colorbars
arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)
# pcolormesh consistent using
pc_kwargs = {'rasterized': True, 'cmap': 'viridis',  'norm': norm}
fig, axs = plt.subplots(3, 3, figsize=(4, 4), layout="constrained")
for ax in axs.flat:
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs[1:, ][:, 1], shrink=0.8)
fig.colorbar(im, ax=axs[:, -1], shrink=0.6)

# suptitle
fig.suptitle('Big Suptitle')

# legends

fig, axs = plt.subplots(1, 2, figsize=(4,2),layout="constrained")

axs[0].plot(np.arange(10))
axs[1].plot(np.arange(10), label='this is a plot')

leg = axs[1].legend(loc='center left', bbox_to_anchor=(0.8,0.5))
#this is usefull to have the legend outside the plot but seen in saveimage
leg.set_in_layout(False)

leg.set_in_layout(True)
fig.set_layout_engine(None)

# padding and spacing

fig,axs =plt.subplots(2,2, layout="constrained")
for ax in axs.flat:
    example_plot(ax, hide_labels=True)
fig.get_layout_engine().set(w_pad=4 / 72, h_pad= 4 / 72, hspace=0, wspace=0)
plt.show()