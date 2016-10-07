import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import seaborn as sns
import plotting as p


def generate_rotation_matrix(angle):
    rot = np.zeros((2, 2))
    rot[0][0] = np.cos(angle)
    rot[0][1] = np.sin(angle)
    rot[1][0] = -np.sin(angle)
    rot[1][1] = np.cos(angle)
    return rot


def rotate_points(pts, angle):
    results = []
    for pt in pts:
        mat = generate_rotation_matrix(angle)
        results.append(np.dot(mat, pt))
    return results


def plot_segments(pts, ax, alpha, c):
    N = len(pts)
    x, y = zip(*pts)
    lines = []
    for i in xrange(N):
        ip1 = (i + 1) % N
        lines.append([(x[i], y[i]), (x[ip1], y[ip1])])

    lc = mc.LineCollection(lines, colors=c, alpha=alpha)
    ax.add_collection(lc)
    pass


def main():
    points = [(-1, -1), (1, -1), (0, np.sqrt(3)-1)]
    fig, ax = plt.subplots(facecolor='black')
    N_angles = 100
    palette = sns.color_palette('cubehelix', N_angles)
    for i, theta in enumerate(np.linspace(0, 2 * np.pi, N_angles)):
        new_points = rotate_points(points, theta)
        plot_segments(new_points, ax, 1-1.0*i/N_angles, palette[i])
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    ax.set_aspect('equal')
    p.remove_axes()
    plt.show()

if __name__ == '__main__':
    main()
