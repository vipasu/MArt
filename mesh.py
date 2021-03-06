import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from matplotlib import rc
import plotting as p

N = 100
numcols = 20

def generate_points(n, xfill=0, yfill=0, xreverse=False, yreverse=True):
    xs, ys = np.linspace(0,1,n), np.linspace(0,1,n)
    if xreverse:
        xs = xs[::-1]
    if yreverse:
        ys = ys[::-1]
    return zip(zip(xs,np.ones(n)*xfill), zip(np.ones(n)*yfill, ys))

fig = plt.figure(figsize=(10,18), facecolor='black')

p.remove_axes()

def plot_segments(segments):
    palette = sns.color_palette('Blues', numcols)
    for i, segment in enumerate(segments):
        plt.plot(segment[0], segment[1], color=palette[i%numcols], alpha=0.5)

lower_left_mesh = generate_points(N, yreverse=True)
plot_segments(lower_left_mesh)
upper_left_mesh = generate_points(N, yfill=1, xreverse=True)
plot_segments(upper_left_mesh)
upper_right_mesh = generate_points(N, xfill=1, yfill=1, yreverse=True)
#plot_segments(upper_right_mesh)
lower_right_mesh = generate_points(N, xfill=1, xreverse=True)
#plot_segments(lower_right_mesh)

#plt.show()
plt.axes().set_aspect('equal')
plt.savefig('mesh.png', facecolor=fig.get_facecolor(), edgecolor='none')
