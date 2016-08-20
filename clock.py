import matplotlib.pyplot as plt
from datetime import datetime

def get_time():
    return datetime.now()  # .gethours, minute


def angle_from_time(hour, minute):
    """
    Returns the angles for both hand and minute
    """

def generate_sweep(theta_i, theta_f):
    """
    Creates a gradient of white to gray such that theta_f is white.
    Accepts:
        - theta_i - initial angle
        - theta_f - final angle
    """

    pass
    # TODO: Decide whether this should sweep the minute hand and hour hand or
    # just the minute

def main():
    h, m = get_time()
    h_theta, m_theta = angle_from_time(h, m)
    plot_hands(h_theta, m_theta)
    delta_t = np.random.uniform(0, 2 * np.pi)
    generate_sweep(m_theta - delta_t, m_theta)

