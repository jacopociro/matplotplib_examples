import numpy as np
import matplotlib.pyplot as plt

def currency(x, pos):
    # the two arguments are the value and tick position
    if x >=1e6:
        s = '$s{:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
        return s

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
# command to make room for elements automatically
plt.rcParams.update({'figure.autolayout': True})

## start
#fig, ax = plt.subplots()
#ax.barh(group_names, group_data)

## controlling the style

#print(plt.style.available)
plt.style.use('fivethirtyeight')
# start
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(group_names, group_data)

## customizing the plot 
labels = ax.get_xticklabels()
# to modify a bunch of stuff
plt.setp(labels, rotation=45, horizontalalignment='right')
# labels
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')

# custom formatting
ax.xaxis.set_major_formatter(currency)

## combining multiple visualization
# add a vertical line
ax.axvline(group_mean, ls='--', color='r')

for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")

# move the title
ax.title.set(y=1.05)

ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=.1)

#print(fig.canvas.get_supported_filetypes())

## Uncomment this to save the figure
#fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
plt.show()