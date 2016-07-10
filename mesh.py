import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from matplotlib import rc
sns.set(font_scale=3.5, rc={'xtick.labelsize': 25,'ytick.labelsize': 25,'legend.fontsize': 25})
sns.set_style('ticks')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

N = 100
numcols = 20

def generate_points(n):
    xs = np.linspace(1./n,1,n)
    ys = xs[::-1]
    return zip(zip(xs,np.zeros(n)), zip(np.zeros(n), ys))

segments = generate_points(N)
fig = plt.figure(figsize=(10,10))
fig.patch.set_visible(False)
ax = plt.gca()
ax.axis('off')
ax.set_xticklabels('')
ax.set_yticklabels('')
ax.set_xticks([])
ax.set_yticks([])


palette = sns.color_palette('husl', numcols)
for i, segment in enumerate(segments):
    plt.plot(segment[0], segment[1], color=palette[i%numcols], alpha=0.5)

plt.show()
