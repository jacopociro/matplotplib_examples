import matplotlib.pyplot as plt
import numpy as np

def first_plot():
    plt.plot([1, 2, 3, 4])
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.ylabel('some numbers')
    plt.show()

def plot_style():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0 , 20])
    plt.show()

def np_array():
    # matplotlib uses numpy arrays
    t = np.arange(0., 5., 0.2)

    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

def keyword_string():
    data = {'a' : np.arange(50),
            'c' : np.random.randint(0, 50, 50),
            'd' : np.random.randn(50)
            }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c = 'c', s ='d', data=data)
    plt.xlabel("entry a")
    plt.ylabel("entry b")
    plt.show()

def categorical_varaibles():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(figsize=(9,3))
    plt.subplot(131)
    plt.bar(names, values)
    
    plt.subplot(132)
    plt.scatter(names, values)

    plt.subplot(133)
    plt.plot(names, values)

    plt.suptitle('Categorical Plotting')
    plt.show()


def line_porperties():
    # not working but these are some of the ways to do it

    plt.plot(x, y, linewidht=2.0)

    line, = plt.plot(x, y, '-')
    line.set_antialiased(False)

    lines = plt.plot(x1, y1, x2, y2)
    plt.setp(lines, color='r', linewidth=2.0)
    plt.setp(lines, 'color', 'r', 'linewidht', 2.0)
    
    # more on the tutorial page

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
def multiple_figures():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    

    plt.figure(2)
    plt.subplot(211)
    plt.plot([1, 2, 3])
    plt.subplot(212)
    plt.plot([4,5,6])

    plt.figure(3)
    plt.plot([4, 5, 6])
    #to make first figure current and modify stuff on it
    plt.figure(1)
    plt.subplot(211)
    plt.title('Easy as 1,2, 3')
    plt.show()

def text():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts', fontsize=14, color='red')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ \n' r'$\sigma_i=15$')
    plt.text(60, .025, r'$\mu=100, \ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    plt.show()

def annotating():
    ax = plt.subplot()

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)
    plt.annotate('local max', xy=(2,1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05),)

    plt.ylim(-2,2)
    plt.show()

def nonlinear_axes():
    np.random.seed(1980801)

    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[( y > 0) & (y < 1)]
    y.sort()
    x=np.arange(len(y))

    plt.figure()

    plt.subplot(221)
    plt.plot(x,y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(x,y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    plt.subplot(223)
    plt.plot(x,y-y.mean())
    plt.yscale('symlog', linthresh=0.01)
    plt.title('symlog')
    plt.grid(True)

    plt.subplot(224)
    plt.plot(x,y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    # this adjust space.
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

    plt.show()

nonlinear_axes()