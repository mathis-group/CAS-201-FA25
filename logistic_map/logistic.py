import numpy as np

def logistic(r, xt):
    xt_plus = r*xt*(1-xt)
    return xt_plus

def run_logistic(r, x0, time_steps):

    # Intialize xs
    xs = [x0]

    for k in range(time_steps+1):
        # Get the next time step
        xt_plus = logistic(r,x0)
        # Record the value in xs by appending
        xs.append(xt_plus)
        # Set x0 to xt_plus
        x0 = xt_plus

    return xs # the value of x from x0 to x_time_steps

def run_logistic_np(r, x0, time_steps):

    # Intialize xs
    xs = np.zeros(time_steps+1)
    xs[0] = x0

    for k in range(1,time_steps+1):
        # Get the next time step
        xs[k] = logistic(r,xs[k-1])

    return xs # the value of x from x0 to x_time_steps

def run_logistic_arrays(r, x0, time_steps):

    # Intialize xs as an array
    xs = np.zeros((len(x0),time_steps+1))
    xs[:,0] = x0

    for t in range(1,time_steps+1):
        # Get the next time step
        xs[:,t] = logistic(r,xs[:,t-1])

    return xs # the value of x from x0 to x_time_steps

if __name__ == "__main__":
    r = 1.8
    x0 = 0.1
    time_steps = 100

    x_over_time = np.round(run_logistic(r, x0, time_steps), 3)
    np_x_over_time = np.round(run_logistic(r, x0, time_steps),3)

    print(np_x_over_time)
    print(x_over_time == np_x_over_time)
