import numpy as np

# Functions we need to use Monte Carlo Methods to compute Pi

# A way to pick random numbers (inside a square)
def random_point():
    x = 2*(np.random.random() - 0.5)
    y = 2*(np.random.random() - 0.5)

    return x,y
# A way to decide if a point is inside a the unit circle (or not)
def is_in_circle(point, r=1.0):
    # Unpack point tuple
    x = point[0]
    y = point[1]
    # Compute d (the distance squared from 0)
    d = x**2 + y**2
    # Decide if inside or outside
    if d <= (r**2):
        return True
    else:
        return False

# Compute the ratio and multiple by 4.

def compute_inside_outside_ratio(num_trials):

    num_inside = 0 # Initialize number of points inside the circle
    for _ in range(num_trials):
        this_point = random_point()
        is_inside = is_in_circle(this_point)
        if is_inside:
            num_inside += 1
    ratio = num_inside/num_trials
    return ratio


if __name__ == "__main__":
    print("Let's compute Pi")
    num_trials = 100_000
    
    ratio = compute_inside_outside_ratio(num_trials)
    print(f"We estimated pi to be {4*ratio} using {num_trials} trials")
    import math
    print(math.pi)