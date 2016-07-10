import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from matplotlib import colors
import hilbert


color_list = ['cyan', 'goldenrod', 'seafoam green', 'light yellow', 'scarlet',
        'neon blue', 'barney purple', 'reddish orange', 'lemon', 'cerise',
        'light lime green', 'teal blue', 'bubblegum pink', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'vermillion', 'amber',
        'melon', 'purpleish', 'bright light blue', 'strawberry', 'celadon']

n_colors = len(color_list)
palette = sns.xkcd_palette(color_list)
cmap = colors.ListedColormap(palette)
bounds = range(n_colors+1)
norm = colors.BoundaryNorm(bounds, cmap.N)

def generate_random_color():
    idx = random.choice(range(n_colors))
    return idx


def plot_hilbert_curve(n, ax):
    locs = hilbert.generate_locations(n)
    for i in xrange(len(locs)-1):
        start, finish = locs[i], locs[i+1]
        xs, ys = zip(start,finish)
        ax.plot(xs, ys, 'white', alpha=0.4, lw='1')


def main(n=32):
    mat = np.zeros((n,n))
    for i in xrange(n):
        for j in xrange(n):
            mat[i][j] = generate_random_color()
    fig = plt.figure(figsize=(15,15), frameon=False)
    ax = fig.add_axes([0,0,1,1])
    ax.axis('off')

    art = ax.imshow(mat, interpolation='nearest', cmap=cmap, norm=norm)
    plot_hilbert_curve(n, ax)
    plt.show()

if __name__ == '__main__':
    main()

