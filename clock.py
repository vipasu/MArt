import matplotlib.pyplot as plt
from datetime import datetime

def get_time():
    d = datetime.now()  # .gethours, minute
    return d.hour, d.minute


def angle_from_time(hour, minute):
    """
    Returns the angles for both hand and minute
    """
    theta_m = minute/float(60)
    hour_angle = 2 * np.pi / 12
    # Adjust for the position of the minute hand
    theta_h = (hour % 12)/float(12) + theta_m/ (2 * np.pi) * hour_angle

    def rotate_to_x_axis(theta):
        """
        Converts angles specified from y axis to ones from x axis
        """
        return np.pi - theta

    return rotate_to_x_axis(theta_h), rotate_to_x_axis(theta_m)


def plot_clock_face():
    """
    Should print just a white circle on black background.
    Possibly add a hint of color (solid or colorwheel)
    Maybe a dot where the 12 should be.
    """
    pass


def plot_hands(theta_h, theta_m):
    hand_lengths = [0.7, 1]
    center = (0, 0)
    for theta, r in zip([theta_h, theta_m], hand_lengths):
        x, y = r * np.cos(theta), r * np.sin(theta)
        plt.plot([0, x], [0, y], 'w')


def generate_sweep(theta_i, theta_f):
    """
    Creates a gradient of white to gray such that theta_f is white.
    Accepts:
        - theta_i - initial angle
        - theta_f - final angle
    """

    pass

def main():
    h, m = get_time()
    h_theta, m_theta = angle_from_time(h, m)
    plot_hands(h_theta, m_theta)
    delta_t = np.random.uniform(0, 2 * np.pi)
    generate_sweep(m_theta - delta_t, m_theta)

