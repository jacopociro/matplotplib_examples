import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def FuncAnimation():
    # func animation method
    global scat, line2, t, z, z2
    fig,ax = plt.subplots()
    t = np.linspace(0, 3, 40)
    g = -9.81
    v0 = 12
    z = g * t**2 / 2 + v0 * t

    v02 = 5
    z2 = g * t**2 / 2 + v02 * t

    scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
    line2 = ax.plot(t[0], z2[0], label = f'v0 = {v02} m/s')[0]
    ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
    ax.legend()

    ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
    plt.show()


def update(frame):
    # for each frrame update the data stored on eanch artist
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot
    data=np.stack([x,y]).T
    scat.set_offsets(data)
    #update the line plot
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])

    return(scat,line2)

def ArtistAnimation():
    # artist animation method
    fig, ax = plt.subplots()
    rng = np.random.default_rng(19689801)
    data = np.array([20, 20, 20, 20])
    x = np.array([1, 2, 3, 4])

    artists =[]
    colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:purple']
    for i in range(20):
        data += rng.integers(low=0, high=10, size=data.shape)
        container = ax.barh(x, data, color=colors)
        artists.append(container)

    ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
    plt.show()

