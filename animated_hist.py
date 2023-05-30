import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(19680801)
HIST_BINS = np.linspace(-4, 4, 100)

data = np.random.randn(1000)
n, _ =  np.histogram(data, HIST_BINS)

