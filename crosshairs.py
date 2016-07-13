import plotting as p
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

N = 1000
numcols = 20

def generate_points(n):
    r = np.clip(np.random.normal(0,.7,n), -1, 1)
    #r = np.clip(np.random.normal(.3,.2,n), -1, 1)
    #r = np.sqrt(np.random.uniform(0,1,n))
    theta = np.random.uniform(0, 2 * np.pi, n)
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    return x, y

def plot_crosshairs(n):
    palette = p.sns.color_palette('husl', numcols)
    p.remove_axes()
    x, y = generate_points(n)
    plt.scatter(x,y,c=palette, s=10, alpha=0.7)
    for i, (x_i,y_i) in enumerate(zip(x,y)):
        plt.axvline(x_i, color=palette[i%numcols], alpha=0.1)
        plt.axhline(y_i, color=palette[i%numcols], alpha=0.1)

fig = plt.figure(figsize=(10,10),facecolor='black')
plot_crosshairs(N)
plt.savefig('CH_gaussian_clipping.png', facecolor=fig.get_facecolor(), edgecolor='none')
