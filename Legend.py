import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

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
plt.show()