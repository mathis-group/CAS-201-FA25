import numpy as np

def logistic (r, xt):
    xt_plus = r * xt * (1 - xt)
    return xt_plus

def run_logistic(r, x0, time_steps):
    xs = [x0]
    for i in range(time_steps + 1):
        xt_plus = logistic(r,x0)
        xs.append(xt_plus)
        x0 = xt_plus
    return xs # the value of x from x0 to x_time_steps

if __name__ == "__main__":
    r = 2.0
    x0 = 0.1
    time_steps = 10

    x_over_time = run_logistic(r, x0, time_steps)
    print(np.round(x_over_time, 2))