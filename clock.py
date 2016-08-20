import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import plotting as p


def get_time():
    d = datetime.now()
    return d.hour, d.minute


def angle_from_time(hour, minute):
    """
    Returns the angles for both hand and minute
    """
    # Angles should be scaled fractions of the full circle
    full_circle = 2 * np.pi
    hour_angle = full_circle / float(12)

    minute_fraction = minute / float(60)
    hour_fraction = (hour % 12) / float(12)

    theta_m =  minute_fraction * full_circle
    # Adjust for the position of the minute hand
    theta_h = hour_fraction * full_circle + minute_fraction * hour_angle

    def rotate_to_x_axis(theta):
        """
        Converts angles specified from y axis to ones from x axis
        """
        return np.pi/2 - theta

    return rotate_to_x_axis(theta_h), rotate_to_x_axis(theta_m)


def plot_clock_face(col='w'):
    """
    Returns polar axes with a solid ring.

    Optionally specify the color of the ring
    """
    p.remove_axes()
    fig = plt.figure(figsize=(10,10), facecolor='k')
    ax = fig.add_subplot(111, polar=True)
    n_points = 100
    ax.plot(np.linspace(0, 2 * np.pi, n_points), n_points * [0.95], color=col,
            alpha=0.3)
    return ax


def plot_hands(theta_h, theta_m, ax, color='w'):
    hand_lengths = [0.5, 0.8]
    for theta, r in zip([theta_h, theta_m], hand_lengths):
        ax.plot([0, theta], [0, r], color)
    return


def generate_sweep(theta_i, theta_f, ax, color='w'):
    """
    Creates a gradient of opacity such that theta_f is opaque.
    Accepts:
        - theta_i - initial angle
        - theta_f - final angle
    """

    rmin, rmax = 0, 0.8
    nslices = 200
    angles = np.linspace(theta_i, theta_f, nslices)
    alphas = np.linspace(0, 1, nslices)**2
    for i in xrange(nslices-1):
        ax.fill_between(angles[i:i+2], 2 * [rmin], 2 * [rmax], alpha=alphas[i], color=color)
    return ax


def main():
    h, m = get_time()
    h_theta, m_theta = angle_from_time(h, m)
    ax = plot_clock_face(p.sns.xkcd_rgb['teal'])
    plot_hands(h_theta, m_theta, ax)
    delta_t = np.random.uniform(0, 2 * np.pi)

    # adding an angle is going counter clockwise (backwards in time)
    generate_sweep(m_theta + delta_t, m_theta, ax)
    p.remove_axes()
