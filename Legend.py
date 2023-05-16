import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from numpy.random import randn
fig,ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label='The red data')
ax.legend(handles=[red_patch], bbox_to_anchor=(1,1), bbox_transform=fig.transFigure)

fig2, ax2 = plt.subplots()
blue_line = mlines.Line2D([], [], color='blue', marker='*', markersize=15, label='Blue stars')

ax2.legend(handles=[blue_line])

# box placement examples
fig3, ax3_dict = plt.subplot_mosaic([['top', 'top'], ['bottom', 'BLANK']], empty_sentinel="BLANK")

ax3_dict['top'].plot([1, 2, 3], label="test1")
ax3_dict['top'].plot([3, 2, 1], label="test2")

ax3_dict['top'].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncols=2, mode="expand", borderaxespad=0.)
ax3_dict['bottom'].plot([1, 2, 3], label="test1")
ax3_dict['bottom'].plot([3, 2, 1], label="test2")

ax3_dict['bottom'].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# figure legends
fig4, axs4 = plt.subplot_mosaic([['left' , 'right']], layout='constrained')
axs4['left'].plot([1, 2, 3], label="test1")
axs4['left'].plot([3, 2, 1], label="test2")

axs4['right'].plot([1, 2, 3], 'C2', label="test3")
axs4['right'].plot([3, 2, 1], 'C3', label="test4")

fig4.legend(loc='upper right')

fig5, ax5 = plt.subplots(figsize=(6, 4), layout='constrained', facecolor='0.7')
ax5.plot([1, 2], [1, 2], label='TEST')
for loc in ['upper left', 'upper center', 'upper right', 'lower left', 'lower center', 'lower right']:
    fig5.legend(loc=loc, title=loc)

fig6, ax6 = plt.subplots(figsize=(6, 4), layout='constrained', facecolor='0.7')
ax6.plot([1, 2], [1, 2], label='test')

for loc in  ['center']:
    fig6.legend(loc=loc, title=loc)

# multiple legends on the sames axes
fig7, ax7 = plt.subplots()
line1, = ax7.plot([1, 2, 3], label="Line 1", linestyle='--')
line2, = ax7.plot([3, 2, 1], label="Line 2", linewidth=4)

first_legend = ax7.legend(handles=[line1], loc='upper right')

ax7.add_artist(first_legend)
ax.legend(handles=[line2], loc='lower right')

# legend handlers
fig8, ax8 = plt.subplots()
line3, = ax8.plot([3, 2, 1], marker='o', label='Line1')
line4, = ax8.plot([1, 2, 3], marker='o', label='Line 2')

ax8.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

z = randn(10)
fig9, ax9 = plt.subplots()
red_dot, = ax9.plot(z, "ro", markersize=15)

white_cross, =ax9.plot(z[:5], "w+", markeredgewidth=3, markersize=15)
ax9.legend([red_dot, (red_dot, white_cross)], ["Attr A", "Attr A+B"])


fig10, ax10 = plt.subplots()
p1, = ax10.plot([1, 2.5, 3], "r-d")
p2, =ax10.plot([3, 2, 1], "k-o")

l = ax10.legend([(p1, p2)], ['Two keys'], numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# custom legend handler

class AnyObject:
    pass

class AnyObjectHandler:
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle([x0, y0], width, height, facecolor='red', edgecolor='black', hatch='xx', lw=3, transform=handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch
    
fig11, ax11 = plt.subplots()
ax11.legend([AnyObject()], ['My first Handler'], handler_map={AnyObject: AnyObjectHandler()})
plt.show()