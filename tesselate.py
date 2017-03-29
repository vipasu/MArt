import numpy as np
import plotting as p


def main(n):
    # Start with a triangle
    p.plt.figure(figsize=(10,10), facecolor='black')
    vertices = generate_vertices(n)
    draw_segments(vertices)
    pick_sub_shape(vertices, depth=5)
    p.remove_axes()
    p.plt.show()
    p.plt.savefig("tesselate_%d_temp.png"%n)
    pass


def generate_vertices(n):
    thetas = np.linspace(np.pi/2, np.pi/2 + 2 * np.pi, n+1)[:n]
    vertices = [np.array([np.cos(theta), np.sin(theta)]) for theta in thetas]
    return vertices


def draw_segments(points):
    n = len(points)
    for i in xrange(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        p.plt.plot([x1, x2], [y1, y2])


def weighted_average(p1, p2, w):
    return w * p1 + (1 - w) * p2


def random_point_on_segment(p1, p2):
    # ran = np.random.uniform(0, 1)
    ran = np.clip(np.random.normal(scale=.2) + .5, 0, 1)
    return weighted_average(p1, p2, ran)


def pick_sub_shape(points, depth=0):
    if depth is 0:
        return

    n = len(points)
    sub_shape_vertices = []
    for i in xrange(n):
        ip1 = (i+1) % n
        sub_shape_vertices.append(random_point_on_segment(points[i], points[ip1]))

    draw_segments(sub_shape_vertices)

    pick_sub_shape(sub_shape_vertices, depth-1)

    # For special case of triangle, you can fill in the other spaces
    # pick_triangles(c1, c12, c31, depth-1)
    # pick_triangles(c2, c12, c23, depth-1)
    # pick_triangles(c3, c23, c31, depth-1)


if __name__ == '__main__':
    main(5)


