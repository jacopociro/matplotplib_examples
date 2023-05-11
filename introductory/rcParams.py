import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

# rc setting
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
# modify multiple rc settings at once
mpl.rc('lines', linewidth=4, linestyle='-.')

data=np.random.randn(50)
#temporary settings
with mpl.rc_context({'lines.linewidth' : 2, 'lines.linestyle' : ':'}):
    plt.plot(data)

#plt.plot(data)

plt.show()