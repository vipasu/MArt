import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc

sns.set(font_scale=3.5, rc={'xtick.labelsize': 25,'ytick.labelsize': 25,'legend.fontsize': 25})
sns.set_style('ticks')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


def remove_axes():
    ax = plt.gca()
    ax.axis('off')
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    ax.set_xticks([])
    ax.set_yticks([])
