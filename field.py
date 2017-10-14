import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotting as p


width = 1.


def create_field(N, yvals):
    """
    Generates a visualization for the strength of the field
    """
    ymax = np.max(yvals)
    ymin = np.min(yvals)
    x_positions = np.linspace(0, width, N+1)
    current_strength = map(field_strength, x_positions)
    plt.plot(x_positions, current_strength, lw=1.5)

    # xv, yv = np.meshgrid(x_positions, y_range)
    # current_strength = map(lambda x : map(field_strength,x), xv)
    # h = plt.hexbin(xv, yv, current_strength)
    # print current_strength

    return min(ymin, np.min(current_strength)), max(ymax,
                                                    np.max(current_strength))


def generate_trajectory(N, vy, eps):
    """
    N - number of points to visit along the way (determines x velocity)
    vy - initial starting velocity
    eps - tolerance around 0 to accept solution
    Returns (success, points)
    success - boolean that denotes whether the boundary condition was met
    within eps
    points - list of points that were taken along the way
    """
    dt = width/N
    x_positions = np.linspace(0, width, N+1)
    current_strength = map(field_strength, x_positions)
    y_positions = np.zeros(N+1)
    for i in range(1, N+1):
        y_positions[i] = y_positions[i-1] + dt * vy
        vy += dt * current_strength[i-1]

    success = (np.abs(y_positions[-1]) < eps)
    return success, y_positions


def field_strength(pos):
    """
    Modify this function to determine how the "current" should flow.
    Assumes that pos takes values between 0 and 1.
    """
    return sin_exp_dec(pos)


def plot_trajectories(trajectories):
    N = len(trajectories[0])
    m = len(trajectories)
    x = np.linspace(0, width, N)
    sns.color_palette('husl', m)
    for i, trajectory in enumerate(trajectories):
        trajectory_frac = float(i)/m
        plt.plot(x, trajectory, alpha=np.sqrt(trajectory_frac),
                 lw=1/(.5 + np.sqrt(trajectory_frac)))
    return


def plot_grid_lines(ymin, ymax):
    print ymax
    n = 7
    for x in np.linspace(0, 1, n+1):
        plt.axvline(x, color='white', linestyle='--', lw=0.5, alpha=0.2)
    for y in np.linspace(ymin, ymax, n+1):
        plt.axhline(y, color='white', linestyle='--', lw=0.5, alpha=0.2)
    return


def main():
    """
    Illustrates the intention behind the shooting method of solving boundary
    problems in differential equations. The physical scenario is one where
    someone tries to cross a river and end up directly across from where he
    started. The "field" mimics the current of the river, which in this case
    may have different directions at different points. The boundary condition
    in this case will be the start and stop positions. The thing that will
    vary across runs is the starting "y" velocity.  The "x" velocity will be
    held constant for now, though in the future it may be extended to be two
    dimensional.
    """
    fig = plt.figure(figsize=(10, 10), facecolor='black')
    p.remove_axes()
    v_0 = 10
    N = 1000
    eps = 0.01
    theta_min, theta_max = -np.pi/2 + 0.05, np.pi/2 - 0.05
    theta = np.random.uniform(theta_min, theta_max)
    trajectories = []

    converged = False
    counter = 0
    # Perform a binary search to find the angle that works
    while not converged and counter < 20:
        print theta
        vy = v_0 * np.arcsin(theta)
        converged, points = generate_trajectory(N, vy, eps)
        trajectories.append(points)
        if points[-1] < 0:  # undershot
            theta_min = theta
        else:
            theta_max = theta
        theta = np.mean([theta_min, theta_max])
        counter += 1
    plot_trajectories(trajectories)
    fmin, fmax = create_field(N, np.concatenate(trajectories))
    plt.axvline(0.5, color='white', alpha=0.2)
    plt.axhline(0, color='white', alpha=0.2)
    plot_grid_lines(fmin, fmax)
    # plt.show()
    plt.savefig('field.png', facecolor=fig.get_facecolor(), edgecolor='none')


def top_hat_with_quadratic(pos):
    if pos < 0.4 or pos > 0.6:
        return -10 * np.abs(0.5 - pos) + 7
    else:
        return 100 * (0.5 - pos)**2


def reverse_heaviside(pos):
    if pos < 0.5:
        return 10
    else:
        return -10


def square_wave(pos):
    bins = np.linspace(0, 1, 11)
    idx = np.digitize(pos, bins)
    if idx % 2 == 0:
        return (10-idx) * 10
    else:
        return -(10-idx) * 10


def sin_exp_dec(pos):
    return 10 * np.exp(-2 * pos) * np.sin(3 * np.pi * pos)


def quartic(pos):
    return (pos) * (3 * pos - 0.33) * (-2 * pos - 0.67) * (5 * pos-1)


if __name__ == '__main__':
    main()
