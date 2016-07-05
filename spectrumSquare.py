import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from matplotlib import colors


color_list = ['cyan', 'goldenrod', 'seafoam green', 'light yellow', 'scarlet',
        'neon blue', 'barney purple', 'reddish orange', 'lemon', 'cerise',
        'light lime green', 'teal blue', 'bubblegum pink', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
        'black', 'black', 'black', 'black', 'black', 'vermillion', 'amber',
        'melon', 'purpleish', 'bright light blue', 'strawberry', 'celadon']

n_colors = len(color_list)
palette = [sns.xkcd_rgb[c] for c in color_list]
cmap = colors.ListedColormap(palette)
bounds = range(n_colors+1)
norm = colors.BoundaryNorm(bounds, cmap.N)

def generate_random_color():
    idx = random.choice(range(n_colors))
    return idx


def main(n=40):
    mat = np.zeros((n,n))
    for i in xrange(n):
        for j in xrange(n):
            mat[i][j] = generate_random_color()
    print mat
    plt.figure(figsize=(15,15))
    art = plt.imshow(mat, interpolation='nearest', cmap=cmap, norm=norm)
    plt.gca().xaxis.set_visible(False)
    plt.gca().yaxis.set_visible(False)
    plt.show()

if __name__ == '__main__':
    main()

