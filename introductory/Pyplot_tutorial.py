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
    