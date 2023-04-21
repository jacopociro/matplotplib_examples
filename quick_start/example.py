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


figures()
