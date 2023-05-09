import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def figure():
    # line in points 1,1 2,4 3,2 4,3
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4], [1,4,2,3])
    plt.show()

def figures():
    # empty figure
    fig1 = plt.figure()
    # figure with one set of axes
    fig2, ax = plt.subplots()
    # figure with 2x2 grid of sets of axes
    fig3, axs1 = plt.subplots(2,2)
    # a figure with one set of axes on the left and two sets of axes on the right
    fig4, axs2 = plt.subplot_mosaic([['left', 'right_top'], ['left', 'right_bottom']])
    plt.show()

def plotting_function():
    # matpotlib to plot function expects numpy.array
    #converting matrix in array
    b = np.matrix([[1,2],[3,4]])
    b_asarray = np.array(b)
    # data keyword argument generates plotspassing the strings corresponding to the x and y variables
    np.random.seed(19680801)
    data = {
        'a' : np.arange(50),
        'c' : np.random.randint(0, 50, 50),
        'd' : np.random.randn(50)
    }

    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100
    
    fig,ax = plt.subplots(figsize=(5, 2.7), layout = 'constrained')
    ax.scatter('a', 'b', c='c',s='d', data=data)
    ax.set_xlabel('entry a')
    ax.set_ylabel('entry b')
    plt.show()

def object_oriented_style():
    # reccomended approach for complex plot
    x = np.linspace(0 ,2, 100)

    fig,ax = plt.subplots(figsize=(5,2.7), layout='constrained')
    ax.plot(x, x, label='linear')
    ax.plot(x, x**2, label='quadratic')
    ax.plot(x, x**3, label='cubic')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title('Simple Plot Object Oriented')
    ax.legend()
    plt.show()
    
def pyplot_style():
    # faster
    x = np.linspace(0, 2, 100)

    plt.figure(figsize=(5,2.7), layout = 'constrained')
    plt.plot(x, x, label='linear')
    plt.plot(x, x**2, label='quadratic')
    plt.plot(x, x**3, label='cubic')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot pyplot style")
    plt.legend()
    plt.show()

def helper_function(ax, data1, data2, param_dict):
    # helper function to make a graph
    out = ax.plot(data1, data2, **param_dict)
    return out
def helper_function_main():
    data1, data2, data3, data4 = np.random.randn(4,100)
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(5,2.7))
    helper_function(ax1, data1, data2, {'marker' : 'x'})
    helper_function(ax2, data3, data4, {'marker': 'o'})
    plt.show()

def styling_artists():
    data1, data2, data3, data4 = np.random.randn(4,100)
    fig,ax = plt.subplots(figsize=(5,2.7))
    x = np.arange(len(data1))
    ax.plot(x,np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
    l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
    l.set_linestyle(':')

    fig1, ax1 = plt.subplots(figsize=(5,2.7))
    ax1.scatter(data1, data2, s = 50, facecolor='C0', edgecolor='k')

    fig2,ax2 = plt.subplots(figsize=(5,2.7))
    ax2.plot(data1, 'o', label = 'data1')
    ax2.plot(data2, 'd', label = 'data2')
    ax2.plot(data3, 'v', label = 'data3')
    ax2.plot(data4, 's', label = 'data4')
    ax2.legend()
    


    plt.show()

def labelling_plots():
    mu, sigma = 115, 15
    x = mu + sigma * np.random.randn(10000)
    fig, ax = plt.subplots(figsize=(5,2.7), layout='constrained')
    n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
    data1, data2, data3, data4 = np.random.randn(4,100)

    ax.set_xlabel('lenght [cm]', fontsize=14, color='red')
    ax.set_ylabel('Probability')
    # mathematical expressions in text
    ax.set_title('Aadvark lenght \n (not really) \n' r'$\sigma_i=15$')
    # to add text in the figure
    ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
    ax.axis([55, 175, 0, 0.03])
    ax.grid(True)

    # annotations
    fig1, ax1 = plt.subplots(figsize=(5, 2.7))
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = ax1.plot(t, s, lw=2)
    # freccia che indica punto di massimo
    ax1.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))  
    ax1.set_ylim(-2,2)
    
    # legends
    fig2, ax2 = plt.subplots(figsize=(5, 2.7))
    ax2.plot(np.arange(len(data1)), data1, label='data1')
    ax2.plot(np.arange(len(data2)), data2, label='data2')
    ax2.plot(np.arange(len(data3)), data3, 'd', label='data3')
    ax2.legend()

    plt.show()

def scales_ticks():
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    data1, data2, data3, data4 = np.random.randn(4,100)
    # scales
    fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
    xdata = np.arange(len(data1))
    data = 10*data1
    axs[0].plot(xdata, data)

    axs[1].set_yscale('log')
    axs[1].plot(xdata, data)
    
    # ticks
    fig1, axs1 = plt.subplots(2, 1, layout='constrained')

    axs1[0].plot(xdata, data)
    axs1[0].set_title('Automatic ticks')

    axs1[1].plot(xdata, data1)
    axs1[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
    axs1[1].set_yticks([-1.5,0,1.5])
    axs1[1].set_title('Manual ticks')

    # plotting dates
    fig2, ax2 = plt.subplots(figsize=(5, 2.7), layout='constrained')
    dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-11-25'), np.timedelta64(1, 'h'))
    data = np.cumsum(np.random.randn(len(dates)))

    ax2.plot(dates, data)
    cdf = mpl.dates.ConciseDateFormatter(ax2.xaxis.get_major_locator())
    ax2.xaxis.set_major_formatter(cdf)

    # plotting strings

    fig3, ax3 = plt.subplots(figsize=(5, 2.7), layout='constrained')
    categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

    ax3.bar(categories, np.random.rand(len(categories)))

    # addiional axis objects
    fig4, (ax4, ax5) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
    l1, = ax4.plot(t, s)
    ax6 = ax4.twinx()
    l2, = ax6.plot(t, range(len(t)), 'C1')
    ax6.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

    ax5.plot(t,s)
    ax5.set_xlabel('Angle [rad]')
    ax7 = ax5.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
    ax7.set_xlabel('Angle[°]')

    plt.show()

def Color_mapped_data():
    data1, data2, data3, data4 = np.random.randn(4,100)

    X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2, - Y**2)

    fig, axs = plt.subplots(2, 2, layout='constrained')
    pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
    fig.colorbar(pc, ax=axs[0, 0])
    axs[0,0].set_title('pcolormesh()')

    co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
    fig.colorbar(co, ax=axs[0, 1])
    axs[0, 1].set_title('contourf()')

    pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
    fig.colorbar(pc, ax=axs[1, 0], extend='both')
    axs[1, 0].set_title('imshow() with LogNorm()')

    pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
    fig.colorbar(pc, ax=axs[1, 1], extend='both')
    axs[1,1].set_title('scatter()')
    plt.show()

def multiple_figures():
    fig, axd = plt.subplot_mosaic([['upleft', 'right'], ['lowleft', 'right']], layout='constrained')
    axd['upleft'].set_title('upleft')
    axd['lowleft'].set_title('lowleft')
    axd['right'].set_title('right')

    plt.show()

